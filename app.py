import base64
import json
import urllib.parse
from requests import post, get
from flask import Flask, render_template, request

# Spotify API credentials
client_id = "client_id"
client_secret = "client_secret"

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = result.json()
    token = json_result["access_token"]
    return token

def get_headers(token):
    return {"Authorization": f"Bearer {token}"}

def search_track(token, track):
    url = "https://api.spotify.com/v1/search"
    headers = get_headers(token)
    params = {
        "q": f"track:{track}",
        "type": "track",
        "market": "IN",
        "limit": 1
    }
    query = urllib.parse.urlencode(params)
    query_url = f"{url}?{query}"
    data = get(query_url, headers=headers).json()
    return data

def get_recommendations(token, track_ids):
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_headers(token)
    params = {
        "seed_tracks": track_ids,
        "limit": 5,
        "market": "IN"
    }
    query = urllib.parse.urlencode(params)
    query_url = f"{url}?{query}"
    json_result = get(query_url, headers=headers).json()
    tracks = json_result.get("tracks")
    if not tracks:
        print("No recommendations found.")
        return None
    return tracks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    track = request.form.get('inputValue')

    response_data = search_track(get_token(), track)
    if not response_data:
        print(f"No track found for {track}.")
        results = []
    else:
        track_id = response_data["tracks"]["items"][0]["id"]
        # Get recommendations for the track
        tracks = get_recommendations(get_token(), track_id)
        if not tracks:
            print(f"No recommendations found for {track}.")
            results = []
        else:
            track_names = [track['name'] for track in tracks]
            results = track_names[:5]

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run()
