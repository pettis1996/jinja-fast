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

posts = [
    {
        "title": "Post 1",
        "content": "Beatae minus ullam ducimus minima magnam non dolores iure? \
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. "
    },
    {
        "title": "Post 2",
        "content": "Beatae minus ullam ducimus minima magnam non dolores iure? \
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. "
    },
    {
        "title": "Post 3",
        "content": "Beatae minus ullam ducimus minima magnam non dolores iure? \
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. "
    },
]

@app.get("/", tags=["home"], description="Returns the home html file for preview.")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts, "dogs": DOGS})