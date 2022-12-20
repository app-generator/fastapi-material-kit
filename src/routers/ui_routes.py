from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

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

# @router.get("/template", status_code=status.HTTP_200_OK)
# def template(request: Request, response_model=HTMLResponse):
#     return TEMPLATES.TemplateResponse("pages/template.html", {"request" : request, "title" : "Template"})


@router.get("/presentation", status_code=status.HTTP_200_OK)
def presentation(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("pages/presentation.html", {"request" : request})


@router.get("/sections/page-sections/hero-sections", status_code=status.HTTP_200_OK)
def hero_sections(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/page-sections/hero-sections.html", {"request" : request})


@router.get("/sections/page-sections/features", status_code=status.HTTP_200_OK)
def features(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/page-sections/features.html", {"request" : request})


@router.get("/sections/navigation/navbars", status_code=status.HTTP_200_OK)
def navbars(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/navigation/navbars.html", {"request" : request})

@router.get("/sections/navigation/nav-tabs", status_code=status.HTTP_200_OK)
def navtabs(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/navigation/nav-tabs.html", {"request" : request})

@router.get("/sections/navigation/pagination", status_code=status.HTTP_200_OK)
def pagination(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/navigation/pagination.html", {"request" : request})

@router.get("/sections/input-areas/inputs", status_code=status.HTTP_200_OK)
def inputs(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/input-areas/inputs.html", {"request" : request})

@router.get("/sections/input-areas/forms", status_code=status.HTTP_200_OK)
def forms(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/input-areas/forms.html", {"request" : request})

@router.get("/sections/attention-catchers/alerts", status_code=status.HTTP_200_OK)
def alerts(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/attention-catchers/alerts.html", {"request" : request})

@router.get("/sections/attention-catchers/modals", status_code=status.HTTP_200_OK)
def modals(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/attention-catchers/modals.html", {"request" : request})

@router.get("/sections/attention-catchers/tooltips_popovers", status_code=status.HTTP_200_OK)
def tooltips_popovers(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/attention-catchers/tooltips-popovers.html", {"request" : request})

@router.get("/sections/elements/avatars", status_code=status.HTTP_200_OK)
def avatars(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/avatars.html", {"request" : request})

@router.get("/sections/elements/badges", status_code=status.HTTP_200_OK)
def badges(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/badges.html", {"request" : request})

@router.get("/sections/elements/breadcrumbs", status_code=status.HTTP_200_OK)
def breadcrumbs(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/breadcrumbs.html", {"request" : request})

@router.get("/sections/elements/buttons", status_code=status.HTTP_200_OK)
def buttons(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/buttons.html", {"request" : request})

@router.get("/sections/elements/dropdowns", status_code=status.HTTP_200_OK)
def dropdowns(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/dropdowns.html", {"request" : request})

@router.get("/sections/elements/progress-bars", status_code=status.HTTP_200_OK)
def progress_bars(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/progress-bars.html", {"request" : request})

@router.get("/sections/elements/toggles", status_code=status.HTTP_200_OK)
def toggles(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/toggles.html", {"request" : request})

@router.get("/sections/elements/typography", status_code=status.HTTP_200_OK)
def typography(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("sections/elements/typography.html", {"request" : request})
