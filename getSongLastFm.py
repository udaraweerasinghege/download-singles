__author__ = 'Udara'
__author__ = 'Pavitheran'
import requests
import json
from bs4 import BeautifulSoup
import youtube_dl
import time
#from download_mp3 import *
from pleer_caler import *

API_KEY = '5b905641511ae41eee7001a79e88775f'

def get_song(artist, num_of_songs = 10):
    response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={0}\
    &autocorrect=1&limit={1}&api_key=5b905641511ae41eee7001a79e88775f&format=json'.format(artist,str(num_of_songs)))
    data = response.json()

    track_list = data['toptracks']['track']
    for track in track_list:
        song = track['name']

        try:
            print(artist + ' '+ song)
        except:
            print(artist + ' ' + 'Unknown Song')

        if '-' in song:
            song = song[:song.index('-')]
        if '/' in song:
            song = song[:song.index('/')]
        if '\\' in song:
            song = song[:song.index('\\')]
        get_mp3(artist + ' ' + song)
        time.sleep(1)
    print('Finished downloading all ' + str(num_of_songs) + ' songs!')

def get_mp3(artist_and_song_name):
    ids = get_tracks(artist_and_song_name)
    api_response = call_pleer_api(ids[0])
    download_url = str(api_response['track_link'])
    file_name = artist_and_song_name + ".mp3"
    download_file(download_url, file_name)


def get_music_vid(artist_and_song):
    source_code = requests.get('http://www.youtube.com/results?search_query=' + artist_and_song)
    plain = source_code.text
    soup = BeautifulSoup(plain)
    links = soup.find_all('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink\
       spf-link '})
    href = "https://www.youtube.com" + links[0].get('href')
    download_link(href)
    print('Finished downloading the music video!')


def download_link(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])




