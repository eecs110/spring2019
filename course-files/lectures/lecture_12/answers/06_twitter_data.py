import urllib.request
import json
import pprint

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

search_term = input('Please enter a search term: ')
url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
request = urllib.request.urlopen(url)
statuses = json.loads(request.read().decode())

tweet_count = 0
tweet_text = ''
for status in statuses:
    if status.get('retweet_count') > tweet_count:
        tweet_count = status.get('retweet_count')
        tweet_text = status.get('text')

print('Most Popular:')
print(tweet_count, tweet_text)
