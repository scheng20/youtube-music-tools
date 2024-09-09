import json
from ytmusicapi import YTMusic
from ytmusic_utils import search_song

ytmusic = YTMusic("oauth.json")

# =================== EXPORT ALL PLAYLISTS =======================
print("-------------- EXPORT ALL PLAYLISTS --------------")

# Step 1: Get all playlists in library
playlists = ytmusic.get_library_playlists(None)
all_playlists = []
exclude_playlists = ["liked music", "recently added", "cop it", "lo-fi vibes", "meh songs", "travel", "guitar", "omori", "episodes"]

for playlist in playlists:
	title = playlist['title']
	if any(substring in title.lower() for substring in exclude_playlists):
		continue
	playlist_id = playlist['playlistId']
	all_playlists.append(dict(title = title, playlistID = playlist_id))

# Step 2: Search each song in each playlist and return its relevant info
all_found_playlists = []

for playlist in all_playlists:

	playlist_title = playlist['title']
	playlist_id = playlist['playlistID']
	playlist_songs = []

	print("PROCESSING PLAYLIST:", playlist_title)

	playlist_tracks = ytmusic.get_playlist(playlist_id)['tracks']

	for track in playlist_tracks:

		# Get the title
		title = track['title']

		# Get the artists
		artists_list = []
		if track['artists'] is not None:
			for artist in track['artists']:
				artists_list.append(artist['name'])
		artists = " ".join(artists_list)

		# Search for it in YTM and add the result to the list
		song_result = search_song(title, artists)
		if song_result is None:
			print("COULD NOT FIND:", title, "by", artists)
			continue

		playlist_songs.append(song_result)

		print("PROCESSED:", title, "by", artists)

	all_found_playlists.append(dict(title = playlist_title, songs = playlist_songs))
	print ("---------------------------------")

# Step 3: Export results to a JSON file
writedata = dict(all_found_playlists = all_found_playlists)
filename = "SC_AllPlaylists.json"

print("WRITING TO FILE:", filename)
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(writedata, f, ensure_ascii=False, indent=4)

print("FINISHED WRITING TO FILE:", filename)
