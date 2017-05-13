# Import Libraries

import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Read Tables

user_data = pd.read_table('datasets/lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv',
                          header = None, nrows = 800000,
                          names = ['users', 'musicbrainz-artist-id', 'artist-name', 'plays'],
                          usecols = ['users', 'artist-name', 'plays'])

user_profiles = pd.read_table('datasets/lastfm-dataset-360K/usersha1-profile.tsv',
                          header = None,
                          names = ['users', 'gender', 'age', 'country', 'signup'],
                          usecols = ['users', 'country'])

# Remove Empty Artist Tuples

if user_data['artist-name'].isnull().sum() > 0:
    user_data = user_data.dropna(axis = 0, subset = ['artist-name'])

# Create Artist Table By Grouping Data According to Artist

artist_plays = (user_data.
     groupby(by = ['artist-name'])['plays'].
     sum().
     reset_index().
     rename(columns = {'plays': 'total_artist_plays'})
     [['artist-name', 'total_artist_plays']]
    )


user_data_with_artist_plays = user_data.merge(artist_plays, left_on = 'artist-name', right_on = 'artist-name', how = 'left')

# Analyse data to find threshold

print artist_plays['total_artist_plays'].describe()
print artist_plays['total_artist_plays'].quantile(np.arange(.9, 1, .01)), 
popularity_threshold = 10000

# Filter populst artist acc to threshold and select United States users

user_data_popular_artists = user_data_with_artist_plays.query('total_artist_plays >= @popularity_threshold')
user_data_popular_artists.head()
combined = user_data_popular_artists.merge(user_profiles, left_on = 'users', right_on = 'users', how = 'left')
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
wide_artist_data = usa_data.pivot(index = 'artist-name', columns = 'users', values = 'plays').fillna(0)
wide_artist_data_sparse = csr_matrix(wide_artist_data.values)

# Import learning algorithms
from sklearn.neighbors import NearestNeighbors

# Randomly select artist
query_index = np.random.choice(wide_artist_data.shape[0])

# Fit filtered data in model
def recommend(algo,dist,inp):
	
	model_knn = NearestNeighbors(algorithm = algo, metric = dist)
	model_knn.fit(inp)

	# Get nearest neighbours
	distances, indices = model_knn.kneighbors(wide_artist_data.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

	# Display the recommended artists
	for i in range(0, len(distances.flatten())):
	    if i == 0:
		print '\n\nRecommendations for {0}:\n'.format(wide_artist_data.index[query_index])
	    else:
		if algo=='brute':		
			print '{0}: {1}, with distance of {2}:'.format(i, wide_artist_data.index[indices.flatten()[i]], distances.flatten()[i])
		else:
			print '{0}: {1}, with distance of {2}:'.format(i, wide_artist_data.index[indices.flatten()[i]], 1-(1/(1+distances.flatten()[i]))) 


recommend('brute','cosine',wide_artist_data_sparse)
recommend('kd_tree','euclidean',wide_artist_data)

print '\n'
