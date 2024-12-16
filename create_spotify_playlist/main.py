import requests
import datetime
import spotipy
from spotipy import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = "ENTER YOUR CLIENT ID"
SPOTIPY_CLIENT_SECRET = "YOUR CLIENT SECRET"
SPOTIPY_REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"

#spotipy documentation - https://spotipy.readthedocs.io/en/2.24.0/

"""checks for date formatting"""
def validate_date_entered(date):
    try:
        datetime.date.fromisoformat(date)
    except:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


"""gets a list of the top 100 songs from a the date entered"""
def get_top_100_songs(date):
    billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(billboard_endpoint)
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")

    song_data = soup.select("li ul li h3")
    song_titles = [song.getText().strip() for song in song_data]
    
    return song_titles


"""gets spotify user id"""
def get_spotify_user_id(spotify):
    user_info = spotify.current_user()              #gets all of the user info from spotify
    user_id = user_info["id"]

    return user_id


"""creates a new playlist in spotify for the current user"""
def create_new_playlist(spotify, user_id, playlist_name):
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)         #creates a new playlist using api
    playlist_id = playlist['id']

    return playlist_id


"""adds song the the newly created playlist"""
def add_songs_to_playlist(spotify, song_titles):
    song_uris = []

    for song in song_titles:

        search = spotify.search(q=f"track: {song} year: 2009", type="track", limit=1, market="US")
        song_uris.append(search['tracks']['items'][0]["uri"])

    spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris, position=None)


date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
validate_date_entered(date_input)

song_titles = get_top_100_songs(date_input)
five_songs = song_titles[:5]

spotify_authentication = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

playlist_name = input("Enter name for the new playlist: ")
spotify_user_id = get_spotify_user_id(spotify_authentication)
playlist_id = create_new_playlist(spotify_authentication, spotify_user_id, playlist_name)

add_songs_to_playlist(spotify_authentication, five_songs)


#2009-04-28