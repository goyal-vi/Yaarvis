import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
cid ="90688df1a331479e8df0cf55248e034d" 
secret = "01640642ee3246919b6083c0f74e6bb8"
username = ""
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
