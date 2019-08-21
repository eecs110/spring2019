from apis import spotify, utilities

tracks = spotify.get_similar_tracks(genres=['pop', 'rock'], simplify=True)
# print(tracks)
df = utilities.get_dataframe(tracks)
print(df)
