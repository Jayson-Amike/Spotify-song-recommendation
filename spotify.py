import spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify API credentials
client_id = '9860b3b9445b47378c732e1cc8110193'
client_secret = '7cbbe3d0379d41f880e713592244a4ee'
redirect_uri = 'http://localhost:8080/callback'

# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotify.Spotify(client_credentials_manager=client_credentials_manager)

# Get a list of recommended tracks based on a seed track
def get_recommendations(seed_track):
    results = sp.recommendations(seed_tracks=[seed_track])
    tracks = results['tracks']
    for track in tracks:
        print(track['name'], 'by', track['artists'][0]['name'])

# Example usage
seed_track = 'spotify:track:6rqhFgbbKwnb9MLmUQDhG6'  # Replace with your own seed track URI
get_recommendations(seed_track)