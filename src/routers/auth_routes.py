from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from src import app
from src.config import settings

import requests

router = APIRouter(
    prefix = "/auth",
    tags = ['Auth']
)

# github Credentials
github_keys = {
    "secret_key"     : settings.github_secret_key,
    "client_id"     : settings.github_client_id,
}

@router.get("/github_login")
async def github_login(request: Request):
    if not settings.github_client_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing a Required Credential, github Client ID, check your environment variables")

    github_login_url = f'https://github.com/login/oauth/authorize?client_id={github_keys["client_id"]}'
    redirect = RedirectResponse(url=github_login_url)
    redirect.status_code = 302
    return redirect


@router.get("/login")
async def authorize_github(request: Request):
    authorization_code = request.query_params.get('code')
    try:        
        url = f'https://github.com/login/oauth/access_token?client_id={github_keys["client_id"]}&client_secret={github_keys["secret_key"]}&code={authorization_code}'
        headers = {
            'accept': 'application/json'
        }
        res = requests.post(url, headers=headers)

        data = res.json()

        access_token = data.get('access_token')

        redirect = RedirectResponse(url=app.ui_router.url_path_for('index'))
        redirect.status_code = 302
        redirect.set_cookie('github-Account', access_token)
        return redirect
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization Code")

@router.get("/user")
async def github_user(request: Request) -> dict:
    access_token = request.cookies.get('github-Account')

    if  (not access_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization Code")

    access_token = 'token ' + access_token
    url = 'https://api.github.com/user'
    headers = {"Authorization": access_token}
    resp = requests.get(url=url, headers=headers)
    userData = resp.json()
    return userData


@router.get("/logout")
def deauthorize_github(request: Request):
    try:
        access_key = request.cookies.get('github-Account')

        if (not access_key):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not logged in.")

        redirect = RedirectResponse(url=app.ui_router.url_path_for('index'))
        redirect.status_code = 302
        redirect.set_cookie('github-Account', '')

        return redirect
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization Code")
