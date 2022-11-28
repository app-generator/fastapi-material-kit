from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from src import app
from src.config import settings
import http3

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


    # NEED TO CHECK THE DOCS ON HOW REDIRECT URI WORKS
    github_login_url = f'https://github.com/login/oauth/authorize?client_id={github_keys["client_id"]}'
    redirect = RedirectResponse(url=github_login_url)
    redirect.status_code = 302
    return redirect

@router.get("/login")
async def authorize_github(request: Request):
    authorization_code = request.query_params.get('code')

    github_authorize_url = f'https://github.com/login/oauth/access_token?client_id={settings.github_client_id}&client_secret={settings.github_secret_key}&code={authorization_code}' 
    get_user_url = "https://api.github.com/user"
    try:

        # here is the main issue
        # during a tsl call, i cannot start a request to.
        # for stripe, this is done with their module.
        # this is my attempt to do it manually        
        http3client = http3.AsyncClient()
        response = await http3client.post(github_authorize_url, authorization_code)

        access_token = response['access_token']

        redirect = RedirectResponse(url=app.ui_router.url_path_for('index'))
        redirect.status_code = 302
        # redirect.set_cookie('github-Account', access_token)

        return redirect
    except Exception as e:
        print (e)
        print ('login error')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Missing Authorization Code")

@router.get("/logout")
def deauthorize_github(request: Request):
    try:
        print (request)
        print (dir(request))
        access_key = request.cookies.get('github-Account')

        if (not access_key):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not logged in")

        redirect = RedirectResponse(url=app.ui_router.url_path_for('index'))
        redirect.status_code = 302
        redirect.set_cookie('github-Account', '')

        return redirect
    except Exception as e:
        print (e)
        # request.cookies.update()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization Code")
