from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

DOGS = [
    {
        "name": "Doggy",
        "type": "Sausage"
    },
    {
        "name": "Snoop Dogg",
        "type": "Stoner"
    }
]

students = [
    {
        "name": "name",
        "password": "password"
    },
    {
        "name": "name1",
        "password": "password1"
    }
]

@app.get("/", tags=["home"], description="Returns the home html file for preview.")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "students": students, "dogs": DOGS})