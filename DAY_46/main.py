import os
import requests
from ytmusicapi import YTMusic
from bs4 import BeautifulSoup

if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
bakeboard_response = requests.get(url)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()

# print(f"Found {len(playlists)} playlists in your library.")
playlist_name = f"{date} Billboard 100"

for playlist in playlists:
    if playlist["title"] == playlist_name:
        print("Playlist Already Exists!")
        break
else:
    playlistId = yt.create_playlist(title=playlist_name,
                                    description=f"This contains the top 100 songs for the year {date}")

    song_list = bakeboard_response.text
    soup = BeautifulSoup(song_list, "html.parser")

    song_title = soup.find_all(name="h3", class_="chart-entry__title")
    song_artist = soup.find_all(name="span", class_="chart-entry__artist")

    titles = [title.text for title in song_title]
    artists = [artist.text for artist in song_artist]
    billboard_list = [f"{title} {artist}" for title, artist in zip(titles, artists)]

    video_id = []
    for item in billboard_list:
        try:
            search_results = yt.search(item)
            for result in search_results:
                if result["resultType"] == "video":
                    video_id.append(result["videoId"])
                    break
        except Exception as e:
            print(f"Skipped: {item} - Reason: {e}")

    yt.add_playlist_items(playlistId, video_id)
    print("Playlist Created Successfully!")
