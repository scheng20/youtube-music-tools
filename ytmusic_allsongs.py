import json
from ytmusicapi import YTMusic
from ytmusic_utils import search_song

ytmusic = YTMusic("oauth.json")

# =================== EXPORT ALL UPLOADED SONGS =======================
print("-------------- EXPORT ALL UPLOADED SONGS --------------")

# Step 1: Get all uploaded songs in library
found_songs = ytmusic.get_library_upload_songs(None, 'a_to_z')

# Step 2: Search each song and return its relevant info
all_found_songs = []
for song in found_songs:

	# Get the title
	title = song['title']

	# Get the artists
	artists_list = []
	if song['artists'] is not None:
		for artist in song['artists']:
			artists_list.append(artist['name'])
	artists = " ".join(artists_list)

	# Get the rating
	rating = song['likeStatus']

	# Search for it in YTM and add the result to the list
	song_result = search_song(title, artists, rating)
	if song_result is None:
		print("COULD NOT FIND:", title, "by", artists)
		continue

	all_found_songs.append(song_result)

	print("PROCESSED:", title, "by", artists)

# Step 3: Export results to a JSON file
writedata = dict(all_found_songs = all_found_songs)
filename = "SC_AllSongs.json"

print("WRITING TO FILE:", filename)
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(writedata, f, ensure_ascii=False, indent=4)

print("FINISHED WRITING TO FILE:", filename)
