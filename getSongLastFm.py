__author__ = 'Udara'
__author__ = 'Pavitheran'
from subprocess import call
import requests
import json
from bs4 import BeautifulSoup
import youtube_dl
import time
#from download_mp3 import *
from pleer_caler import *

API_KEY = '5b905641511ae41eee7001a79e88775f'

def clean_up(song):
    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    song = song.strip(punctuation)
    if song.upper() == 'JAYZ':
        return 'Jay-Z'
    if song.upper() == 'KE$HA':
        return 'ke$ha'
    if song.upper() == '3OH!3':
        return '3oh!3'
    if '-' in song:
        return song[:song.index('-')]
    if '/' in song:
        return song[:song.index('/')]
    if '\\' in song:
        return song[:song.index('\\')]


    return song

def get_song(artist, num_of_songs = 5):
    if not(isinstance(num_of_songs, int)):
        print("Invalid number of songs, defaulted to five")
        num_of_songs = 5
    response = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={0}\
    &autocorrect=1&limit={1}&api_key=5b905641511ae41eee7001a79e88775f&format=json'.format(artist,str(num_of_songs)))
    data = response.json()
    try:
        track_list = data['toptracks']['track']
        for track in track_list:
            song = track['name']
            song_dl = (artist + ' '+ song)
            try:
                get_mp3(song_dl)
                print("Downloaded: {}\n".format(song))
                time.sleep(1)
            except:
                print("Could not find song: {}\n".format(song))
                num_of_songs -= 1
        print('Successfully downloaded ' + str(num_of_songs) + ' songs!')
    except:
        print("Artist {} not found".format(artist))


def get_charts_top(num=5):
    if not(isinstance(num, int)):
        print("Invalid number of songs, defaulted to five")
        num_of_songs = 5
    response = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&limit={}&\
    api_key=5b905641511ae41eee7001a79e88775f&format=json".format(str(num)))
    data = response.json()
    songs = data['tracks']['track']
    for song in songs:
        song_name = song['name']
        artist = song['artist']['name']
        to_download = artist + " " + song_name
        try:
            get_mp3(to_download)
            print("Downloaded: {0} by {1}\n".format(song_name, artist))
            time.sleep(1)
        except:
            print("Could not find the song: {}\n".format(song_name))
            num -= 1

    print('Finished downloading all ' + str(num) + ' songs')


def get_mp3(artist_and_song_name):
    artist_and_song_name = clean_up(artist_and_song_name)
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
    href = "https://www.youtube.com" + links[1].get('href')
    print(href)
    download_link(href)
    print('Finished downloading the music video!')


def download_link(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

