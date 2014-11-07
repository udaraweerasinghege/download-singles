__author__ = 'Pavitheran'
import requests
from bs4 import BeautifulSoup
import youtube_dl


def get_singles(artist_name):
    source_code = requests.get('http://en.wikipedia.org/wiki/{0}'.format(under_scores(artist_name)))
    soup = BeautifulSoup(source_code.content)
    table = soup.find('span', id='Singles').parent.find_next_sibling('table')
    for single in table.find_all('th', scope='row'):
        get_youtube_link(artist_name + single.text)

def under_scores(name):
    split = name.split()
    result = ''
    for part in split:
        if split.index(part) != len(split)-1:
            result += part + '_'
        else:
            result += part
    result += '_discography'
    return result


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
