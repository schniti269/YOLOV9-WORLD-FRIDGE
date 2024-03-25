from fastapi import FastAPI, HTTPException, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.config import Config

from db import get_db, User, Recipe

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


@app.get("/login")
async def login(request: Request):
    # Redirect to GitHub for login
    redirect_uri = request.url_for('auth')
    return await oauth.github.authorize_redirect(request, redirect_uri)

@app.get("/oauth/callback")
async def auth(request: Request, db=Depends(get_db)):
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
    
        return "Created",{"username": user_info['login'], "user_id": user_info['id']}
    else:
        return "Logged in",{"username": user_info['login'], "user_id": user_info['id']}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)