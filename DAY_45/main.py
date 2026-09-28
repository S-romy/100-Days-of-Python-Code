import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/"
                        "features/best-movies-2/")

content = response.text
soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies.reverse()

file = open("Top 100 movies of all time.txt", "w", encoding="utf-8")
for movie in movies:
    text = movie.getText()
    file.write(f"{text}\n")

file.close()
