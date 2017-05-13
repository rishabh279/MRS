from User_Data import User_Data as ud

class Popular_Artist:
	# Remove Empty Artist Tuples

	if ud.person_data['artist-name'].isnull().sum() > 0:
	    ud.person_data = ud.person_data.dropna(axis = 0, subset = ['artist-name'])

	# Create Artist Table By Grouping Data According to Artist

	singer_plays = (ud.person_data.
	     groupby(by = ['artist-name'])['plays'].
	     sum().
	     reset_index().
	     rename(columns = {'plays': 'total_artist_plays'})
	     [['artist-name', 'total_artist_plays']]
	    )


	person_data_with_singer_plays = ud.person_data.merge(singer_plays, left_on = 'artist-name', right_on = 'artist-name', how = 'left')

