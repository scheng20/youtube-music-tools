from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")

# =================== HELPER FUNCTIONS =======================
def search_song(title, artist, rating=None):
	query = " ".join((title, artist))
	result = ytmusic.search(query, "songs")
	if result is None or len(result) < 1:
		return None

	top_result = ytmusic.search(query, "songs")[0]
	result_title = top_result['title']
	video_id = top_result['videoId']
	add_feedback_token = top_result['feedbackTokens']['add']

	song = dict(
		title = result_title,
		artist = artist,
		rating = rating,
		videoID = video_id,
		addFeedbackToken = add_feedback_token
	)

	return song

def add_song_to_library(videoID, addFeedbackToken, rating=None):
	add_response = ytmusic.edit_song_library_status(addFeedbackToken)
	rate_response = ytmusic.rate_song(videoID, rating)

