import requests
from bs4 import BeautifulSoup


endpoint = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(endpoint)
website_data = response.text
soup = BeautifulSoup(website_data, "html.parser")

movies_data = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movies_titles = [movie.getText() for movie in movies_data]
# movies_ranked = list(reversed(movies_ranked))
movies_ranked = movies_titles[::-1]

with open("movies.txt", "w") as file:
    for movie in movies_ranked:
        file.write(f"{movie}\n")
