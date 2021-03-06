import urllib.request
import json
import pprint

# write a program that:
# 1. Prompts the user for a search term
# 2. Queries Twitter for status updates based on the search term
# 3. Iterates through the resulting data dictionary and
# 4. Prints the text of the status and the number of times it has been retweeted

search_term = input('Please enter a search term: ')
url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
request = urllib.request.urlopen(url)
statuses = json.loads(request.read().decode())

for status in statuses:
    print(status.get('retweet_count'), status.get('text'), '\n')