import urllib.request
from urllib.request import urlopen
import json
import pandas as pd
import collections
from pprint import pprint
from .spotify_formatter import SpotifyFormatter


class Spotify(SpotifyFormatter):
    def __init__(self):
        self.token = self._get_token()

    # Handles security:
    def _get_token(self):
        url = 'https://www.apitutor.org/spotify/key' # authenticates to Spotify
        results = urlopen(url).read().decode('utf-8', 'ignore')
        return json.loads(results)['token']

    # retrieves data from any Spotify endpoint:
    def _issue_get_request(self, url):
        request = urllib.request.Request(url, None, {
            'Authorization': 'Bearer ' + self.token
        })
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            return data
    
    def get_tracks(self, search_term:str, simplify:bool=True):
        '''
        Retrieves a list of Spotify tracks, given the search term passed in.
          * search_term (str): [Required] A search term (for a song), represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of tracks.
        '''
        search_term = urllib.parse.quote_plus(search_term)
        url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_tracks(data['tracks']['items'])

    def get_tracks_by_artist(self, artist_id:str, simplify:bool=True):
        '''
        Retrieves a list of Spotify "top tracks" by an artist
          * artist_id (str): [Required] The Spotify id of the artist, represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of tracks.
        '''
        url = 'https://api.spotify.com/v1/artists/' + artist_id + '/top-tracks?country=us'
        # print(url)
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_tracks(data['tracks'])

    def get_tracks_by_playlist(self, playlist_id:str, simplify:bool=False):
        url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
        # print(url)
        data = self._issue_get_request(url)
        if not simplify:
            return data
        
        def get_track(item):
            return item['track']
        tracks = list(map(get_track, data['items']))
        return self.simplify_tracks(tracks)

    def get_related_artists(self, artist_id:str, simplify:bool=True):
        '''
        Retrieves a list of artists related to the artist you specify
          * artist_id (str): [Required] The Spotify id of the artist, represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of artists.
        '''
        url = 'https://api.spotify.com/v1/artists/' + artist_id + '/related-artists'
        # print(url)
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_artists(data['artists'])

    def get_artists(self, search_term:str, simplify:bool=True):
        '''
        Retrieves a list of Spotify artists, given the search term passed in.
          * search_term (str): [Required] A search term (for an artist), represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of artists.
        '''
        search_term = urllib.parse.quote_plus(search_term)
        url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_artists(data['artists']['items'])

    def get_playlists(self, search_term:str, simplify:bool=True):
        '''
        Retrieves a list of Spotify tracks, given the search term passed in.
          * search_term (str): [Required] A search term (for a song), represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of tracks.
        '''
        search_term = urllib.parse.quote_plus(search_term)
        url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=playlist'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_playlists(data['playlists']['items'])

    def get_playlists_by_user(self, user_id:str, simplify:bool=True):
        '''
        Retrieves a list of Spotify tracks, given the search term passed in.
          * search_term (str): [Required] A search term (for a song), represented as a string.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of tracks.
        '''
        url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self.simplify_playlists(data['items'])

    def get_audio_features_by_track(self, track_id:str):
        url = 'https://api.spotify.com/v1/audio-features/' + track_id
        return self._issue_get_request(url)

    def get_similar_tracks(self, artist_ids:str=None, track_ids:str=None, simplify=False):   
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
        data = self._issue_get_request(url)
        if not simplify:
            return data
    
        return self.simplify_tracks(data['tracks'])
