import urllib.request
from urllib.request import urlopen
import json
import pandas as pd
import collections
from apis import authentication


API_TUTOR_TOKEN = 'API.fda8c628-f8f0-448d-aad8-42c2fcd067ec'


def get_tracks(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks']['items'])

def get_tracks_by_artist(artist_id:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify "top tracks" by an artist
        * artist_id (str): [Required] The Spotify id of the artist.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/top-tracks?country=us'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks'])

def get_tracks_by_playlist(playlist_id:str, simplify:bool=False):
    '''
    Retrieves a list of the tracks associated with a playlist_id
        * playlist_id (str): [Required] The id of the Spotify playlist.
        * simplify (bool):   Whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    
    def get_track(item):
        return item['track']
    tracks = list(map(get_track, data['items']))
    return _simplify_tracks(tracks)

def get_related_artists(artist_id:str, simplify:bool=True):
    '''
    Retrieves a list of artists related to the artist you specify
        * artist_id (str): [Required] The Spotify id of the artist, represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of artists.
    '''
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/related-artists'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_artists(data['artists'])

def get_artists(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify artists, given the search term passed in.
        * search_term (str): [Required] A search term (for an artist), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of artists.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_artists(data['artists']['items'])

def get_playlists(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=playlist'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_playlists(data['playlists']['items'])

def get_playlists_by_user(user_id:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_playlists(data['items'])

def get_audio_features_by_track(track_id:str):
    '''
    Retrieves Spotify's audio analysis of the track.
        * track_id (str): [Required] The id of the Spotify track.
    Returns a list of audio features.
    '''
    url = 'https://api.spotify.com/v1/audio-features/' + track_id
    return _issue_get_request(url)

def get_similar_tracks(artist_ids:str=None, track_ids:str=None, simplify=False): 
    '''
    Spotify's way of providing recommendations. Either artist_ids or track_ids (or both) is required.
        * artist_ids (str): A comma-delimited list of artists
        * track_ids (str): A comma-delimited list of tracks
    Returns a list of tracks that are similar
    '''
        # a comma-delimited list of artists
        # a comma-delimited list of tracks
    if not artist_ids and not track_ids:
        raise Exception('Either artist_ids or track_ids is required')
    params = []
    if artist_ids:
        params.append('seed_artists=' + artist_ids)
    if track_ids:
        params.append('seed_tracks=' + track_ids)
    
    url = 'https://api.spotify.com/v1/recommendations?' + '&'.join(params)
    data = _issue_get_request(url)
    if not simplify:
        return data

    return _simplify_tracks(data['tracks'])


#############################
# Some formatting utilities #
#############################

def get_track_player_html(track_id:int):
    '''
    Creates the HTML tags for a Spotify player.
        * track_id (int): [Required] The id of a track.
    Returns an HTML iFrame  (str) corresponding to a Spotify player for the track. 
    '''
    return '''
    <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
    </iframe>
    '''.format(track_id=track_id)

def get_playlist_player_html(playlist_id:int, width:int=400, height:int=280):
    return '''
    <iframe src="https://open.spotify.com/embed/playlist/{playlist_id}" 
        width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
        allow="encrypted-media">
    </iframe>'''.format(playlist_id=playlist_id, width=width, height=height)

def get_album_player_html(album_id:int, width:int=300, height:int=380):
    return '''
    <iframe src="https://open.spotify.com/embed/album/{album_id}" 
        width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
        allow="encrypted-media">
    </iframe>'''.format(album_id=album_id, width=width, height=height)

def get_image_html(image_url:str):
    '''
    Creates an image (HTML)
        * image_url (str): [Required] The url of the image.
    Returns an HTML image tag (str).
    '''
    from IPython.display import Image
    return Image(url=image_url)._repr_html_()

def flatten_for_pandas(data:list):
    flattened_list = []
    count = 1
    for item in data:
        item = _flatten(item)
        item['num'] = count
        flattened_list.append(item)
        count += 1
    return flattened_list
    
def get_dataframe(data:list):
    flattened_list = flatten_for_pandas(data)
    return pd.DataFrame(flattened_list).set_index('num')

def get_jupyter_styling():
    return """
        <style>
            .rendered_html img { 
                display: inline-block; 
                vertical-align: baseline;
                max-width: 200px !important;
                margin-right: 20px !important;
            }
            .rendered_html td, .rendered_html th { text-align: left !important; }
        </style>
        """



############################################
# Some private, helper functions utilities #
############################################
# retrieves data from any Spotify endpoint:
def _issue_get_request(url):
    token = authentication.get_token('https://www.apitutor.org/spotify/key')
    request = urllib.request.Request(url, None, {
        'Authorization': 'Bearer ' + token
    })
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode())
        return data

def _simplify_tracks(tracks:list):
    try:
        tracks[0]
    except Exception:
        return tracks

    simplified = []
    for item in tracks:
        track = { 
            'id': item['id'], 
            'name': item['name'], 
            'preview_url': item['preview_url'],
            'share_url': 'https://open.spotify.com/track/' + item['id']
        }
        try:
            track['album'] = {
                'id': item['album']['id'],
                'name': item['album']['name'],
                'image_url': item['album']['images'][0]['url'],
                'image_url_small': item['album']['images'][-1]['url'],
                'share_url': 'https://open.spotify.com/album/' + item['album']['id']
            }
        except Exception:
            pass
        try:
            artist = item['album']['artists'][0]
            track['artist'] = { 
                'id': artist['id'], 
                'name': artist['name'],
                'share_url': 'https://open.spotify.com/artist/' + item['album']['artists'][0]
            }
        except Exception:
            pass
        simplified.append(track)
    return simplified

def _simplify_artists(artists:list):
    try:
        artists[0]
    except Exception:
        return artists

    simplified = []
    for item in artists:
        artist = { 
            'id': item['id'], 
            'name': item['name'], 
            'genres': ', '.join(item['genres']),
            'share_url': 'https://open.spotify.com/artist/' + item['id']
        }
        try:
            artist['image_url'] = item['images'][0]['url']
            artist['image_url_small'] = item['images'][-1]['url']
        except Exception:
            pass
        simplified.append(artist)
    return simplified

def _simplify_playlists(playlists:list):
    try:
        playlists[0]
    except Exception:
        return playlists
    simplified = []
    for item in playlists:
        simplified.append({ 
            'id': item['id'], 
            'name': item['name'], 
            'owner_display_name': item['owner']['display_name'],
            'owner_id': item['owner']['id'],
            'share_url': 'https://open.spotify.com/playlist/' + item['id']
        })
    return simplified

def _flatten(d:dict, parent_key:str='', sep:str='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(_flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)