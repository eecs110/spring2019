import pandas as pd
import collections


class SpotifyFormatter(object):

    def flatten(self, d:dict, parent_key:str='', sep:str='_'):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(self.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
  
    def simplify_tracks(self, tracks:list):
        try:
            tracks[0]
        except Exception:
            return tracks

        simplified = []
        for item in tracks:
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

    def simplify_artists(self, artists:list):
        try:
            artists[0]
        except Exception:
            return artists

        simplified = []
        for item in artists:
            artist = { 
                'id': item['id'], 'name': item['name'], 'genres': ', '.join(item['genres'])
            }
            try:
                artist['image_url'] = item['images'][0]['url']
                artist['image_url_small'] = item['images'][-1]['url']
            except Exception:
                pass
            simplified.append(artist)
        return simplified

    def simplify_playlists(self, playlists:list):
        try:
            playlists[0]
        except Exception:
            return playlists
        simplified = []
        for item in playlists:
            simplified.append({ 
                'id': item['id'], 'name': item['name'], 
                'owner_display_name': item['owner']['display_name'],
                'owner_id': item['owner']['id']
            })
        return simplified

        # renders the spotify HTML player (by track ID)
    
    def get_track_player_html(self, track_id:int):
        '''
        Creates the HTML tags for a Spotify player.
          * track_id (int): [Required] The id of a track.
        Returns an HTML iFrame  (str) corresponding to a Spotify player for the track. 
        '''
        return '''
        <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
        </iframe>
        '''.format(track_id=track_id)

    def get_playlist_player_html(self, playlist_id:int, width:int=400, height:int=280):
        return '''
        <iframe src="https://open.spotify.com/embed/playlist/{playlist_id}" 
            width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
            allow="encrypted-media">
        </iframe>'''.format(playlist_id=playlist_id, width=width, height=height)

    def get_album_player_html(self, album_id:int, width:int=300, height:int=380):
        return '''
        <iframe src="https://open.spotify.com/embed/album/{album_id}" 
            width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
            allow="encrypted-media">
        </iframe>'''.format(album_id=album_id, width=width, height=height)

    def get_image_html(self, image_url:str):
        '''
        Creates an image (HTML)
          * image_url (str): [Required] The url of the image.
        Returns an HTML image tag (str).
        '''
        from IPython.display import Image
        return Image(url=image_url)._repr_html_()

    def flatten_for_pandas(self, data:list):
        flattened_list = []
        count = 1
        for item in data:
            item = self.flatten(item)
            item['num'] = count
            flattened_list.append(item)
            count += 1
        return flattened_list
        
    def get_dataframe(self, data:list):
        flattened_list = self.flatten_for_pandas(data)
        return pd.DataFrame(flattened_list).set_index('num')

    def get_jupyter_styling(self):
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