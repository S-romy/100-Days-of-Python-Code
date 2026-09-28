from bs4 import BeautifulSoup
# import lxml

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)
