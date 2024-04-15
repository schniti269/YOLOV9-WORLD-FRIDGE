from fastapi import FastAPI, HTTPException, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from jose import jwt
from datetime import datetime, timedelta
from typing import List
from fastapi import Cookie

import pandas as pd
import os
import cv2
import base64

from models import RecipeCreate, image64

from starlette.responses import Response

from matcher import match, add_recipe

from db import get_db, User, Recipe, Ingredient, image_to_base64

from predictor import run_inference_on_image

app = FastAPI()

SECRET_KEY = "hallo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#cors
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
# Initialize OAuth
oauth = OAuth()
# Configure GitHub OAuth
oauth.register(
    name='github',
    client_id='110250731c4d9f59bb8a',
    client_secret='c37a6d7cb7bf9707899a637ff969e533ce713ecd',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


def cookie_auth(request: Request,cookie: str = Cookie(None, alias='user')):
    token = cookie
    if token is None:
        print("no token raising HTTPException")
        raise HTTPException(status_code=401, detail="Unauthorized/no token")
    try:
        print("decoding token")
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user= payload["user_id"]
        #no user in the token
        if user is None:
            #this should not happen unless the token is tampered with but just in case
            raise HTTPException(status_code=401, detail="Unauthorized")
       
        #check if user exists in the database
        db=next(get_db())
        if db.query(User).filter(User.oauth_id == user).first() is None:
            #this should not happen unless the token is tampered with but just in case
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        return user
    except:
        #this should not happen unless the token is tampered with
        print("error decoding token")
        raise HTTPException(status_code=401, detail="Unauthorized/invalid token")

@app.get("/login")
async def login(request: Request):
    # Redirect to GitHub for login
    redirect_uri = request.url_for('auth')
    return await oauth.github.authorize_redirect(request, redirect_uri)

@app.get("/oauth/callback")
async def auth(request: Request, response: Response, db=Depends(get_db)):
    # GitHub redirects back here after login
    try:
        token = await oauth.github.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail="OAuth Authentication Failed")

    resp = await oauth.github.get('user', token=token)
    user_info = resp.json()

    # Check if user is in the database
    user = db.query(User).filter(User.oauth_id == user_info['id']).first()

    if user is None:
        # Create a new user
        user = User(oauth_id=user_info['id'],username=user_info['login'])
        db.add(user)
        db.commit()

    # Save user with auth cookie
    jwt_user = {
        "user_id": user.oauth_id,
        "exp": datetime.now() + timedelta(minutes=30)
    }

    token = jwt.encode(jwt_user, SECRET_KEY, algorithm=ALGORITHM)
    response.set_cookie("user", token, httponly=True)
    return "Created",{"username": user_info['login'], "user_id": user_info['id']}

@app.get("/logout")
async def logout(response: Response):
    response.delete_cookie("user")
    return "Logged out"

###functions
@app.get("/recipes")
async def get_recipes(db=Depends(get_db)):
    recipes = db.query(Recipe).all()
    return recipes

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int, db=Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.post("/recipes")
async def add_recipe(recipe: RecipeCreate, user: int = Depends(cookie_auth), db=Depends(get_db)):
    add_recipe(recipe.name, recipe.description, recipe.instructions, recipe.ingredients, recipe.image64)
    #query for the recipe
    recipe = db.query(Recipe).filter(Recipe.name == recipe.name).first()
    #add to user
    user = db.query(User).filter(User.oauth_id == user).first()
    user.owned_recipes.append(recipe.id)
    return recipe

@app.get("/me/favourite_recipes")
async def get_user_recipes(user: int = Depends(cookie_auth), db=Depends(get_db)):
    favourites= db.query(User).filter(User.oauth_id == user).first().favourite_recipes
    recipes = []
    for recipe in favourites:
        recipe = db.query(Recipe).filter(Recipe.id == recipe).first()
        recipes.append(recipe)
    return recipes

@app.post("/me/favourite_recipes/{recipe_id}")
async def add_user_recipe(recipe_id: int, user: int = Depends(cookie_auth), db=Depends(get_db)):
    user = db.query(User).filter(User.oauth_id == user).first()
    user.favourite_recipes.append(recipe_id)
    db.commit()
    return "Added to favourites"

@app.delete("/me/favourite_recipes/{recipe_id}")
async def remove_user_recipe(recipe_id: int, user: int = Depends(cookie_auth), db=Depends(get_db)):
    user = db.query(User).filter(User.oauth_id == user).first()
    user.favourite_recipes.remove(recipe_id)
    db.commit()
    return "Removed from favourites"

@app.get("/me/owned_recipes")
async def get_user_recipes(user: int = Depends(cookie_auth), db=Depends(get_db)):
    owned= db.query(User).filter(User.oauth_id == user).first().owned_recipes

    recipes = []
    for recipe in owned:
        recipe = db.query(Recipe).filter(Recipe.id == recipe).first()
        recipes.append(recipe)
    return recipes

@app.post("/match")
async def get_matches(items: List[str], db=Depends(get_db)):
    #match
    matches = match(items)
    return matches

@app.post("/scan")
async def scan_fridge(image: image64, db=Depends(get_db)):
    #get from image 64 object
    base64_image = image.image64
    #convert to PIL
    image = base64.b64decode(base64_image)
    #save image
    with open("temp.jpg", "wb") as img_file:
        img_file.write(image)
    #open as cv2
    image = cv2.imread("temp.jpg")
    #remove temp file
    os.remove("temp.jpg")


    #run inference
    items, annotated_image = run_inference_on_image(image)
    base64_image = image_to_base64(annotated_image,binary_mode=True)

    items = [{"name":name, "count":count} for name,count in items.items()]
    return {"items":items ,"image":base64_image}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)