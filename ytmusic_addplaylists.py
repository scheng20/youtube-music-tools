import json
from ytmusicapi import YTMusic
from ytmusic_utils import add_song_to_library

ytmusic = YTMusic("oauth.json")

# =================== ADD PLAYLISTS TO LIBRARY =======================
print("-------------- ADD PLAYLISTS TO LIBRARY --------------")

# Step 1: Read playlist info from file
filename = "SC_AllPlaylists_Missed.json"

with open(filename, 'r', encoding='utf-8') as file:
    readdata = json.load(file)

all_found_playlists = readdata['all_found_playlists']

# Step 2: Create playlist and add songs to it

for playlist in all_found_playlists:
	playlist_title = playlist['title']
	playlist_songs = playlist['songs']

	playlist_id = ytmusic.create_playlist(playlist_title, "Test description")

	all_song_video_ids = []

	for song in playlist_songs:
		all_song_video_ids.append(song['videoID'])
	
	ytmusic.add_playlist_items(playlist_id, all_song_video_ids)
	print("PROCESSED: ", playlist_title)
