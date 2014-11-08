__author__ = 'Udara'
import requests
import json

API_KEY = '5b905641511ae41eee7001a79e88775f'
SECRET = 'cf537d2466ff4f57cabdf762db1bf980'

def get_song(artist):
    response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={0}\
    &autocorrect=1&limit=10&api_key=5b905641511ae41eee7001a79e88775f&format=json'.format(artist))
    data = response.json()


    track_list = data['toptracks']['track']
    for track in track_list:
        print(track['name'])

get_song('ladygaga')