from flask import Flask
from flask import render_template
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1,10)
    year = datetime.now().year
    #adding random_number as a parameter after the index file allow for the html file to access the python variable
    return render_template("index.html", num=random_number, current_year=year)


@app.route("/guess/<name>")
def guess(name):
    gender_guess_data = requests.get(url=f"https://api.genderize.io?name={name}").json()
    gender_guess = gender_guess_data["gender"]

    age_guess_data = requests.get(url=f"https://api.agify.io?name={name}").json()
    age_guess = age_guess_data["age"]

    return render_template("guess.html", name=name.title(), gender=gender_guess, age=age_guess)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_data = requests.get(url="https://api.npoint.io/79f7e7b1b1644e20f810").json()

    return render_template("blog.html", blog=blog_data)


if __name__ == "__main__":
    app.run(debug=True)

home()