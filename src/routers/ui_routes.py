from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import http3


# from src import app
# import src.oauth2 as oauth2
# from src.config import Settings
# from src import models, schemas


router = APIRouter(
    tags = ['User Interface']
)


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))

@router.get("/", status_code=status.HTTP_200_OK)
def index(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/index.html", {"request" : request})


@router.get("/about-us", status_code=status.HTTP_200_OK)
def about_us(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/about-us.html", {"request" : request})

@router.get("/contact-us", status_code=status.HTTP_200_OK)
def contact_us(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/contact-us.html", {"request" : request})


@router.get("/author", status_code=status.HTTP_200_OK)
def author(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/author.html", {"request" : request})


@router.get("/sign-in", status_code=status.HTTP_200_OK)
def sign_in(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/sign-in.html", {"request" : request})

