import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SCOPE = (
    "user-read-email "   
    "user-top-read "
    "user-read-recently-played "
    "playlist-read-private "
    "user-library-read "
) # "_ " as spotify expeccts scope as space separated string

def get_spotify_auth():
    return SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True, 
        cache_path=".spotify_cache"  
    )

def get_spotify_client():
    auth_manager = get_spotify_auth()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def get_user_info(sp):
    user_profile = sp.current_user()
    user_data = {
        "display_name": user_profile.get("display_name"),
        "email": user_profile.get("email"),
        "id": user_profile.get("id"),
        "country": user_profile.get("country"),
        "profile_image": user_profile['images'][0]['url'] if user_profile['images'] else None
    }
    return user_data