import urllib.request
from urllib.request import urlopen
import json

class YouTube(object):
    def __init__(self):
        self.token = self._get_token()

    # Handles security:
    def _get_token(self):
        url = 'https://www.apitutor.org/youtube/key' # authenticates to Spotify
        results = urlopen(url).read().decode('utf-8', 'ignore')
        return json.loads(results)['token']
    
    def _simplify(self, data):
        try:
            data['items'][0]
        except Exception:
            return data

        simplified = []
        for item in data['items']:
            simplified.append({
                'videoId': item['id']['videoId'],
                'thumb_url': item['snippet']['thumbnails']['high']['url'],
                'title': item['snippet']['title'],
                'url': 'https://www.youtube.com/watch?v=' + item['id']['videoId'],
                'embed_url': 'https://www.youtube.com/embed/' + item['id']['videoId']
            })
        return simplified


    def get_videos(self, search_term, simplify=True):
        '''
        Retrieves a list of YouTube videos.
          * search_term (str): Required search term
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of YouTube videos.
        '''
        search_term = urllib.parse.quote_plus(search_term)
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + search_term + '&type=video&key=' + self.token
        response = urlopen(url)
        data = json.loads(response.read().decode('utf-8', 'ignore'))
        if not simplify:
            return data
        return self._simplify(data)

    def get_video_player_html(self, embed_url, width=560, height=315):
        '''
        Returns an HTML IFrame (str). Requires an embed_url (string) argument.
        '''

        return '''
        <iframe width="{width}" height="{height}" src="{embed_url}" 
            frameborder="0" 
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
        '''.format(width=width, height=height, embed_url=embed_url)

    def get_image_html(self, image_url):
        '''
        Returns an HTML image (str). Requires an image_url (string) argument.
        '''
        from IPython.display import Image
        return Image(url=image_url)._repr_html_()