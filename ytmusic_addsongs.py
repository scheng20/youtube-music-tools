import json
from ytmusicapi import YTMusic
from ytmusic_utils import add_song_to_library

ytmusic = YTMusic("oauth.json")

# =================== ADD SONGS TO LIBRARY =======================
print("-------------- ADD SONGS TO LIBRARY --------------")

# Step 1: Read song info from file
filename = "SC_AllSongs.json"

with open(filename, 'r', encoding='utf-8') as file:
    readdata = json.load(file)

all_found_songs = readdata['all_found_songs']

# Step 2: Add songs to library
for song in all_found_songs:
	add_song_to_library(song['videoID'], song['addFeedbackToken'], song['rating'])
	print("PROCESSED: ", song['title'], "by", song['artist'])
