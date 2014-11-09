__author__ = 'Udara'


"""Simple script that scrapes pleer's search results page for MP3s
and lets you download them.
"""

import requests
##from tabulate import tabulate
from bs4 import BeautifulSoup

PLEER_API_URL = 'http://pleer.com/site_api/files/get_url'

def call_pleer_api(song_id):
    post_data = {'action': 'download', 'id': song_id}
    response = requests.post(PLEER_API_URL, params=post_data)
    return response.json()


def download_file(url, local_filename):
    print('Downloading file')
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    print('Finished downloading file')


def get_tracks(search_string):
    song_ids = []
    url = 'http://pleer.com/search?q={0}&target=tracks&page=1'.format(search_string)
    page_content = requests.get(url)
    raw_html = page_content.text
    soup = BeautifulSoup(raw_html)
    results = soup.findAll('div', {'class': 'playlist'})
    for song_listing in results:
        songs = song_listing.findChildren('li')
        for song in songs:
            song_ids.append(str(song.get('link')))
    return song_ids



"""
ids = (get_tracks('taylor swift love story',1))
print(ids)
api_response = call_pleer_api(ids[0])
print(api_response)
z = (api_response['track_link'])
#download_url = str(api_response['track_link'])
artist = 'taylor swift'
song = 'fifteen'
file_name = artist + ' ' + song + '.mp3'
##whatf going on??
download_file(z, file_name)
"""