import requests
from bs4 import BeautifulSoup

URL = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
# print(soup.prettify())

movie_titles = soup.find_all(name="h1", class_="list-item__title")
# print(movie_titles)
list_of_movies = [title.getText() for title in movie_titles]
print(list_of_movies)

counter = 100
with open("hollywood_reporter_list_movies.txt", "w") as file:
    for movie in list_of_movies:
        file.write(f"{counter} {movie}\n")
        counter -= 1
