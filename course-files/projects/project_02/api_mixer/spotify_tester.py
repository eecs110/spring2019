from apis import spotify
from pprint import pprint

help(spotify)

playlists = spotify.get_playlists_by_user('spotify', simplify=True)
pprint(playlists, depth=3)

# playlists = spotify.get_playlists('cut copy', simplify=False)
# pprint(playlists, depth=5)

# item = data[0]
# track_id = item['id']
# img_url = item['album']['image_url']

# iframe = spotify.get_track_player_html(track_id)
# print(iframe)

# img = spotify.get_image_html(img_url)
# print(img)