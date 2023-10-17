import requests
import os
#from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
AUTH_URL = 'https://accounts.spotify.com/api/token'

#Load Tracks Information

soja_uri = 'spotify:artist:2vaWvC8suCFkRXejDOK7EE'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_top_tracks(soja_uri)

top_tracks = results['tracks'][:10]

#Convert to DataFrame

names = []
popularity = []
duration_ms = []

for track in top_tracks:
    names.append(track['name'])
    popularity.append(track['popularity'])
    duration_ms.append(track['duration_ms'])

top_tracks_df = pd.DataFrame({
    'name': names,
    'popularity': popularity,
    'duration': duration_ms
    })

#Convert to Numerical and Change miliseconds to minutes

top_tracks_df['popularity'] = top_tracks_df['popularity'].astype(float)
top_tracks_df['duration'] = top_tracks_df['duration'].astype(int)

top_tracks_df['duration'] = top_tracks_df['duration'] / 60000


#Sort by Popularity
top_tracks_df = top_tracks_df.sort_values(by='popularity', ascending=False)

#Get the Top 3
print(top_tracks_df.head(3))

#Scatter Plot is shown on the Notebook.ipynb
















# 1) Connect to the database here using the SQLAlchemy's create_engine function

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function