from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import spotipy
import sys
import spotipy.util as util 
import pprint
from datetime import datetime
import json

with open('config.json') as config_file:
    data = json.load(config_file)

cid = data['cid']
secret = data['secret']
username = data['username']

redirect_uri = 'http://localhost/'
todays_date = str(datetime.date(datetime.now()))

url = "https://www.grimeys.com/new-releases/1-17-20"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, 'html.parser')

release_div = page_soup.find(id="block-6e7b1a860960c3a8334c")

releases = release_div.find_all('strong')

list_of_releases = []

for release in releases:
    artist = release.text
    album = release.next_sibling.replace('-', ' ').strip().split('CD/')
    artist_album = (artist.replace(',', '.') + ' ' + album[0])
    list_of_releases.append(artist_album)

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)

def create_playlist():
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlist = sp.user_playlist_create(username, 'New Songs from ' + todays_date, description=('a playlist of songs released on ' + todays_date))
        playlist_id = playlist['id']
        album_ids = []
        for release in list_of_releases:
            result = sp.search(q = release, type = 'album')
            if len(result['albums']['items']) > 0:
                album_id = result['albums']['items'][0]['uri']
                album_ids.append(album_id)
            else:
                continue
        for album in album_ids:
            tracks = sp.album_tracks(album)
            track_list = []
            for track in tracks['items']:
                track_list.append(track['id'])
            for track in track_list:
                sp.user_playlist_add_tracks(username, playlist_id, ['spotify:track:' + track])
    else:
        print("Can't get token for", username)

create_playlist()

