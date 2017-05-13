# Import Libraries

import pandas as pd


class User_Data:
	pd.set_option('display.float_format', lambda x: '%.3f' % x)

	# Read Tables

	person_data = pd.read_table('datasets/lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv',
		                  header = None, nrows = 800000,
		                  names = ['users', 'musicbrainz-artist-id', 'artist-name', 'plays'],
		                  usecols = ['users', 'artist-name', 'plays'])

	person_profiles = pd.read_table('datasets/lastfm-dataset-360K/usersha1-profile.tsv',
		                  header = None,
		                  names = ['users', 'gender', 'age', 'country', 'signup'],
		                  usecols = ['users', 'country'])

