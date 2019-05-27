from apis import youtube

help(youtube)

data = youtube.get_videos('puppies')
# data = youtube.get_videos('puppies', simplify=False)
# print(data)

embed_url = data[0]['embed_url']
thumb_url = data[0]['thumb_url']
iframe = youtube.get_video_player_html(embed_url, width=420)
print(iframe)

# img = youtube.get_image_html(thumb_url)
# print(img)