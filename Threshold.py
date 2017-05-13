from Popular_Artist import Popular_Artist as pa
import numpy as np

class Threshold:
	# Analyse data to find threshold

	print pa.singer_plays['total_artist_plays'].describe()
	print pa.singer_plays['total_artist_plays'].quantile(np.arange(.9, 1, .01)), 
	popularity_threshold = 10000

	# Filter populst artist acc to threshold and select United States users

	person_data_popular_singer = pa.person_data_with_singer_plays.query('total_artist_plays >= @popularity_threshold')
	person_data_popular_singer.head()

