from apis import yelp
import pprint

help(yelp)

# businesses = yelp.get_businesses(categories='italian', location='Tallahassee, FL', limit=5)
# pprint.pprint(businesses, indent=3)

# print()
# for business in businesses:
#     print(
#         business.get('name'), 
#         business.get('rating'), 
#         business.get('price'), 
#         business.get('review_count')
#     )

# print()
# print(yelp.get_categories())

# print()
# business = businesses[0]
# pprint.pprint(yelp.get_reviews(business['id']))