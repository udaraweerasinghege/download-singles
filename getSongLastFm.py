__author__ = 'Udara'
import requests
import json
from bs4 import BeautifulSoup
import youtube_dl
import time
from download_mp3 import *

API_KEY = '5b905641511ae41eee7001a79e88775f'

def get_song(artist, num_of_songs = 10):
    response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={0}\
    &autocorrect=1&limit={1}&api_key=5b905641511ae41eee7001a79e88775f&format=json'.format(artist,str(num_of_songs)))
    data = response.json()

    track_list = data['toptracks']['track']
    for track in track_list:
        song = track['name']
        print(artist+ ' ' + song)
        get_mp3(artist + ' ' + song)
        time.sleep(2)

def get_mp3(artist_and_song_name):
    ids = get_tracks(artist_and_song_name,1)
    api_response = call_pleer_api(ids[0])
    download_url = str(api_response['track_link'])
    file_name = artist_and_song_name + " " + ".mp3"
    download_file(download_url, file_name)


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

"""song_list =['taylor swift Shake It Off','taylor swift We Are Never Ever Getting Back Together','taylor swift I Knew You Were Trouble','taylor swift 22','taylor swift Red','taylor swift Love Story','taylor swift You Belong with Me','taylor swift All Too Well','taylor swift Out of the Woods','taylor swift State of Grace']
for song in song_list:
    print(song)
    get_mp3(song)
"""



