from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
def get_song_list():
    global date
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(billboard_url)
    billboard_web_page = response.text

    soup = BeautifulSoup(billboard_web_page, "html.parser")
    song_titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
    song_list = []

    for song in song_titles:
        song = song.text.replace("\n", "").replace("\t", "")
        song_list.append(song)

    title1 = soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")
    cleaned_title1 = title1.getText().replace("\n", "").replace("\t", "")
    song_list.insert(0, cleaned_title1)
    return song_list

# def playlist_exists():
#     sp = spotipy.Spotify(
#         auth_manager=SpotifyOAuth(
#             scope="playlist-read-private",
#             redirect_uri="http://example.com",
#             client_id=os.getenv("CLIENT_ID"),
#             client_secret=os.getenv("CLIENT_SECRET"),
#             show_dialog=True,
#             cache_path="token.txt",
#             username=os.getenv("USERNAME")
#         )
#     )
#     existing_playlists = sp.current_user_playlists(50)
#     for i in range(0, (existing_playlists['total'] - 2)):
#         if existing_playlists['items'][i]['name'] == "Musical Time Machine" and existing_playlists['items'][i]['tracks']['total'] != 0:
#             print("Looks like the playlist is already created.")
#             return True
#         else:
#             print("Your playlist will be created shortly")
#             return False

def create_playlist():
    song_list = get_song_list()
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            show_dialog=True,
            cache_path="token.txt",
            username=os.getenv("USERNAME")
        )
    )

    uri_list = []

    user_id = sp.current_user()["id"]

    for song in song_list:
        result = sp.search(q=f"track:{song}", type="track", limit=1, market="IN")
        try:
            uri_list.append(result['tracks']['items'][0]['uri'])
        except IndexError or KeyError:
            print(f"{song} not found on Spotify")

    playlist_details = sp.user_playlist_create(user_id, "Musical Time Machine", False)
    playlist_id = playlist_details["id"]
    sp.playlist_add_items(playlist_id, uri_list)
    print("Tracks added successfully")


# if not playlist_exists():
    create_playlist()



