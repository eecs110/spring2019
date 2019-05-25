from apis import yelp
import pprint

help(yelp)

data = yelp.get_businesses(sort_by='review_count', limit=10, simplify=True, categories='italian')

print()
pprint.pprint(data, indent=3)

print()
for item in data:
    print(item.get('name'), item.get('rating'), item.get('price'), item.get('review_count'))

print()
print(yelp.categories)

print()
pprint.pprint(yelp.get_comments(data[1]['id']))