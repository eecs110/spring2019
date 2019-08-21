import urllib.request
from urllib.request import urlopen
import json

# Handles security:
def get_token():
    url = 'https://www.apitutor.org/spotify/key' # authenticates to Spotify
    results = urlopen(url).read().decode('utf-8', 'ignore')
    return json.loads(results)['token']

# retrieves data from any Spotify endpoint:
def _retrieve_from_spotify(url):
    request = urllib.request.Request(url, None, {
        'Authorization': 'Bearer ' + get_token()
    })
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode())
        return data
    
def _simplify_tracks(data):
    # print(data)
    try:
        data['tracks']['items'][0]
    except Exception:
        return data

    simplified = []
    for item in data['tracks']['items']:
        track = { 'id': item['id'], 'name': item['name'], 'preview_url': item['preview_url'] }
        try:
            track['album'] = {
                'id': item['album']['id'],
                'name': item['album']['name'],
                'image_url': item['album']['images'][0]['url'],
                'image_url_small': item['album']['images'][-1]['url']
            }
        except Exception:
            pass
        try:
            artist = item['album']['artists'][0]
            track['artist'] = { 'id': artist['id'], 'name': artist['name'] }
        except Exception:
            pass
        simplified.append(track)
    return simplified

def _simplify_artists(data):
    try:
        data['artists']['items'][0]
    except Exception:
        return data

    simplified = []
    for item in data['artists']['items']:
        artist = { 
            'id': item['id'], 'name': item['name'], 'genres': item['genres']
        }
        try:
            artist['image_url'] = item['images'][0]['url']
            artist['image_url_small'] = item['images'][-1]['url']
        except Exception:
            pass
        simplified.append(artist)
    return simplified

# retrieves tracks:
def get_tracks(search_term, simplify=True):
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
    data = _retrieve_from_spotify(url)
    if not simplify:
        return data
    return _simplify_tracks(data)

# retrieves artists:
def get_artists(search_term, simplify=True):
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
    data = _retrieve_from_spotify(url)
    if not simplify:
        return data
    return _simplify_artists(data)

# renders the spotify HTML player (by track ID)
def make_player(track_id):
    return '''
    <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
    </iframe>
    '''.format(track_id=track_id)

# renders an image (with URL argument)
def make_image_html(image_url):
    from IPython.display import Image
    return Image(url=image_url)._repr_html_()