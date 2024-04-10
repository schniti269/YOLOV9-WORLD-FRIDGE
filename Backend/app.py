from fastapi import FastAPI, HTTPException, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config
from jose import jwt
from datetime import datetime, timedelta

import base64

from models import Recipe, image64

from starlette.responses import Response

from matcher import match, add_recipe

from db import get_db, User, Recipe

from predictor import run_inference_on_image

app = FastAPI()

# Setup Session Middleware with a secret key
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

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

def cookie_auth(request: Request):
    token = request.cookies.get("user")
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        user= payload["user_id"]
        if user is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
        #db query
        db=next(get_db())
        if db.query(User).filter(User.oauth_id == user).first() is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return user
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")

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
    token = jwt.encode(jwt, "secret", algorithm="HS256")
    response.set_cookie(key="user", value=str(token), httponly=True, max_age=1800,secure=True)
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
async def add_recipe(recipe: Recipe, user: int = Depends(cookie_auth), db=Depends(get_db)):
    add_recipe(recipe.name, recipe.description, recipe.instructions, recipe.ingredients, recipe.image64)
    return "Recipe added"


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



@app.get("/match")
async def get_matches(image: image64, db=Depends(get_db)):
    #convert image to base64
    base64_image = image.image64
    #convert to PIL
    image = base64.b64decode(base64_image)

    #run inference
    items, annotated_image = run_inference_on_image(image)
    

    #match
    matches = match(items)

    base64_image = base64.b64encode(annotated_image).decode('utf-8')
    return matches, base64_image











if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)