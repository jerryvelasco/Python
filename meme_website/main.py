from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import json
import requests

#initialize fastapi app
app = FastAPI()

#network request
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_text = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_text, subreddit

#setup jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    meme_picture, subrredit = get_meme()
    return templates.TemplateResponse("index.html", {"request": request, "meme_picture": meme_picture, "subreddit": subrredit})
