from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import requests

#initialize fastapi app
app = FastAPI()

#setup jinja2 templates
templates = Jinja2Templates(directory="templates")

#weather api
API_KEY = "ENTER YOUR API KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API key}

#gets weather data using the city name as input
def get_weather(city: str):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }

    response = requests.get(BASE_URL, params=parameters)

    #will be passed to template if found for display 
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

        return weather
    
    else:
        return None
    
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "weather": None 
    })

#gets triggered after submitting the form, the city is sent as part of the request to get weather info
@app.post("/", response_class=HTMLResponse)
async def weather(request: Request, city: str = Form(...)):
    weather_data = get_weather(city)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "weather": weather_data
    })
