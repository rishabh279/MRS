from Threshold import Threshold as th
from User_Data import User_Data as ud
from scipy.sparse import csr_matrix

class Country:
	combined = th.person_data_popular_singer.merge(ud.person_profiles, left_on = 'users', right_on = 'users', how = 'left')
	usa_data = combined.query('country == \'United States\'')
	usa_data.head()

	# Remove duplicate rows
	if not usa_data[usa_data.duplicated(['users', 'artist-name'])].empty:
	    initial_rows = usa_data.shape[0]

	    print 'Initial dataframe shape {0}'.format(usa_data.shape)
	    usa_data = usa_data.drop_duplicates(['users', 'artist-name'])
	    current_rows = usa_data.shape[0]
	    print 'New dataframe shape {0}'.format(usa_data.shape)
	    print 'Removed {0} rows'.format(initial_rows - current_rows)

	# Convert matrix into sparse matrix
	sparse_singer_data = usa_data.pivot(index = 'artist-name', columns = 'users', values = 'plays').fillna(0)
	sparse_singer_data_compress = csr_matrix(sparse_singer_data.values)


