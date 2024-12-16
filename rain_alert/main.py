import requests
import smtplib
import os

api_key = os.environ.get("OPEN_WEATHER_API_KEY")

parameters = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "mode": "json",
    "cnt": 4
}

my_email = "jerrycoding1@gmail.com"  
my_password = os.environ.get("MY_PASSWORD")

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(f"HTTP status code: {response.status_code}")

will_rain = False

#checks if its raining based on the weather codes provided in openweather documentation
for weather in data["list"]:
    weather_ids = weather["weather"][0]["id"]

    if int(weather_ids) < 700:
        will_rain = True

if will_rain:

    #only sends email if weather codes are below a certain marker 
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="jerrycoding1@yahoo.com",
            msg="Subject:Ahhh it's raining!\n\n\nDont't forget an umbrella. It's going to rain today!!"
        )


