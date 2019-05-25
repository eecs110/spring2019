import urllib.request
from urllib.request import urlopen
import json

# https://www.yelp.com/developers/documentation/v3/business_search
class Yelp(object):
    def __init__(self):
        self.token = self._get_token()
        self.categories = [
            'mexican', 'sandwiches', 'breakfast_brunch', 'chinese', 'restaurants', 
            'food', 'mexican', 'sandwiches', 'breakfast_brunch', 'nightlife', 
            'bars', 'chinese', 'pizza', 'coffee', 'burgers', 'cafes', 'newamerican', 
            'hotdogs', 'japanese', 'tradamerican', 'foodtrucks', 'sushi', 'salad', 
            'vietnamese', 'delis', 'thai', 'seafood', 'italian', 'indpak', 
            'asianfusion', 'bbq', 'vegan', 'korean', 'noodles', 'bakeries', 
            'chicken_wings', 'mediterranean', 'cocktailbars', 'desserts', 
            'eventservices', 'vegetarian', 'foodstands', 'hotdog', 'latin', 
            'ethiopian', 'soup', 'juicebars', 'catering', 'gluten_free', 
            'soulfood', 'beerbar', 'himalayan', 'mideastern', 'ramen', 'tacos', 
            'sportsbars', 'tapasmallplates', 'wine_bars', 'french', 'grocery', 
            'gourmet', 'arts', 'comfortfood', 'diners', 'dimsum', 'southern', 
            'cajun', 'cantonese', 'caribbean', 'chickenshop', 'pubs', 'buffets', 
            'icecream', 'pakistani', 'poke', 'popuprestaurants', 'shopping', 
            'bagels', 'brazilian', 'donuts', 'gastropubs', 'greek', 'halal', 
            'streetvendors', 'hawaiian', 'creperies', 'filipino', 'venues', 
            'beer_and_wine', 'cheesesteaks', 'salvadoran', 'szechuan', 
            'waffles', 'african', 'bubbletea', 'fishnchips', 'peruvian', 
            'beergardens', 'burmese', 'falafel', 'musicvenues', 'spanish', 
            'convenience', 'german', 'izakaya', 'laotian', 'lounges', 'meats', 
            'tapas', 'breweries', 'cafeteria', 'hotpot', 'kebab', 'steak', 
            'taiwanese', 'tex-mex'
        ]
        self.categories.sort()

    # Handles security:
    def _get_token(self):
        url = 'https://www.apitutor.org/yelp/key' # authenticates to Spotify
        results = urlopen(url).read().decode('utf-8', 'ignore')
        return json.loads(results)['token']

    # retrieves data from any Spotify endpoint:
    def _issue_get_request(self, url):
        request = urllib.request.Request(url, None, {
            'Authorization': 'Bearer ' + self.token
        })
        try:
            with urllib.request.urlopen(request) as response:
                data = json.loads(response.read().decode())
                return data
        except urllib.error.HTTPError as e:
            error_message = e.read()
            error_message = '\n' + str(e) + '\n' + str(json.loads(error_message)) + '\n'
            raise Exception(error_message)
    
    def _simplify_businesses(self, data):
        simplified = []
        for item in data['businesses']:
            business = {
                'id': item['id'],
                'name': item['name'],
                'rating': item['rating'],
                'image_url': item['image_url'],
                'display_address': '., '.join(item['location']['display_address']),
                'coordinates': item['coordinates'],
                'review_count': item['review_count']
            }
            try:
                business['price'] = item['price']
            except:
                pass
            simplified.append(business)
        return simplified

    def _simplify_comments(self, data):
        simplified = []
        for item in data['reviews']:
            review = {
                'id': item['id'],
                'rating': item['rating'],
                'text': item['text'],
                'time_created': item['time_created'],
                'url': item['url']
            }
            simplified.append(review)
        return simplified

    def get_businesses(self, location='Evanston, IL', limit=20, 
            term=None, categories=None, sort_by=None, price=None, open_now=None,
            simplify=True):
        '''
        Searches for Yelp businesses based on various search criteria
        '''

        url = 'https://api.yelp.com/v3/businesses/search?location=' + \
            urllib.parse.quote_plus(location) + '&limit=' + str(limit)
        if term:
            url += '&term=' + urllib.parse.quote_plus(term)
        if categories:
            url += '&categories=' + urllib.parse.quote_plus(categories)
        if sort_by:
            # if sort_by not in ['best_match', 'rating', 'review_count', 'distance']:
            #     raise Exception(sort_by + " not in ['best_match', 'rating', 'review_count', 'distance']")
            url += '&sort_by=' + urllib.parse.quote_plus(sort_by)
        if price:
            url += '&price=' + str(price)  #1, 2, 3, 4 -or- 1,2 (for more than one)
        if open_now:
            url += '&open_now=true' 

        print(url)       

        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self._simplify_businesses(data)

    def get_comments(self, business_id, simplify=True):
        # https://www.yelp.com/developers/documentation/v3/business_reviews
        url = 'https://api.yelp.com/v3/businesses/' + business_id + '/reviews'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self._simplify_comments(data)

    # renders an image (with URL argument)
    def get_image_html(self, image_url):
        from IPython.display import Image
        return Image(url=image_url)._repr_html_()