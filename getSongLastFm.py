__author__ = 'Udara'
import requests
import json
from bs4 import BeautifulSoup
import youtube_dl
from download_mp3 import *

API_KEY = '5b905641511ae41eee7001a79e88775f'
SECRET = 'cf537d2466ff4f57cabdf762db1bf980'

def get_song(artist):
    response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={0}\
    &autocorrect=1&limit=10&api_key=5b905641511ae41eee7001a79e88775f&format=json'.format(artist))
    data = response.json()


    track_list = data['toptracks']['track']
    for track in track_list:
        song = track['name']
        print(artist+ ' ' + song)
        get_mp3(artist + ' ' + song)

def get_mp3(artist_and_song_name):
    ids = get_tracks(artist_and_song_name,1)
    api_response = call_pleer_api(ids[0])
    download_url = str(api_response['track_link'])
    file_name = artist_and_song_name + " " + ".mp3"
    download_file(download_url,file_name)



"""
def get_youtube_link(artist_and_song):
    source_code = requests.get('http://www.youtube.com/results?search_query=' + artist_and_song)
    plain = source_code.text
    soup = BeautifulSoup(plain)
    links = soup.find_all('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink  \
       spf-link '})
    href = "https://www.youtube.com" + links[0].get('href')
    download_link(href)


def download_link(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
"""