__author__ = 'Udara'
import requests
import json

API_KEY = '5b905641511ae41eee7001a79e88775f'
SECRET = 'cf537d2466ff4f57cabdf762db1bf980'

response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=cher&\
autocorrect=1&api_key=5b905641511ae41eee7001a79e88775f&format=json')
data = response.json()


track_list = data['toptracks']['track']
print(type(track_list))
for track in track_list:
    print(track['name'])
