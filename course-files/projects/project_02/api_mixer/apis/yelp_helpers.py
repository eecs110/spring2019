import urllib.request
from urllib.request import urlopen
import json

# https://www.yelp.com/developers/documentation/v3/business_search
class Yelp(object):
    def __init__(self):
        self.token = self._get_token()

    def get_categories(self):
        '''
        Returns all of the available restaurant categories that the user
        can filter by on Yelp.
        '''
        categories = [
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
        categories.sort()
        return categories

    # Handles security:
    def _get_token(self):
        url = 'https://www.apitutor.org/yelp/key' # authenticates to Spotify
        results = urlopen(url).read().decode('utf-8', 'ignore')
        return json.loads(results)['token']

    # retrieves data from any Spotify endpoint:
    def _issue_get_request(self, url:str):
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
    
    def _simplify_businesses(self, data:list):
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

    def _simplify_comments(self, data:list):
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

    def get_businesses(self, location:str='Evanston, IL', limit:int=20, 
            term:str=None, categories:str=None, sort_by:str=None, price:int=None, open_now:str=None,
            simplify:bool=True):
        '''
        Searches for Yelp businesses based on various search criteria, including:
        
          * location (str):   Location of the search
          * limit (int):      An integer indicating how many records to return. Max of 50.
          * term (str):       A search term
          * categories (str): One or more comma-delimited categories to filter by.
          * sort_by (str):    How to order search results. Options are: 
                              best_match, rating, review_count, distance
          * price (int):      How expensive 1, 2, 3, 4 or comma-delimited list, e.g.: 1,2
          * open_now (str):   Set to 'true' if you only want the open restaurants
          * simplify (bool):  Indicates whether you want to simplify the data that is returned.

        Returns a list of businesses matching your search / ordering / limit criteria.
        '''

        url = 'https://api.yelp.com/v3/businesses/search?location=' + \
            urllib.parse.quote_plus(location) + '&limit=' + str(limit)
        if term:
            url += '&term=' + urllib.parse.quote_plus(term)
        if categories:
            url += '&categories=' + urllib.parse.quote_plus(categories)
        if sort_by:
            if sort_by not in ['best_match', 'rating', 'review_count', 'distance']:
                raise Exception(sort_by + " not in ['best_match', 'rating', 'review_count', 'distance']")
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

    def get_reviews(self, business_id:int, simplify:bool=True):
        '''
        Retrieves a list of Yelp reviews for a particular business.
          * business_id (int): [Required] An integer corresponding to the business id.
          * simplify (bool):   Indicates whether you want to simplify the data that is returned.
        Returns a list of reviews.
        '''
        # https://www.yelp.com/developers/documentation/v3/business_reviews
        url = 'https://api.yelp.com/v3/businesses/' + business_id + '/reviews'
        data = self._issue_get_request(url)
        if not simplify:
            return data
        return self._simplify_comments(data)

    def get_image_html(self, image_url:str):
        '''
        Returns an HTML image tag (str). Requires an image_url (string) argument.
        '''
        from IPython.display import Image
        return Image(url=image_url)._repr_html_()