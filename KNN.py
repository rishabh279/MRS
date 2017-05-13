from Country import Country as co
import numpy as np
from sklearn.neighbors import NearestNeighbors


# Randomly select artist
query_index = np.random.choice(co.sparse_singer_data.shape[0])

# Fit filtered data in model
def recommend(algo,dist,inp):
	
	model_knn = NearestNeighbors(algorithm = algo, metric = dist)
	model_knn.fit(inp)

	# Get nearest neighbours
	distances, indices = model_knn.kneighbors(co.sparse_singer_data.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

	# Display the recommended artists
	for i in range(0, len(distances.flatten())):
	    if i == 0:
		print '\n\nRecommendations for {0}:\n'.format(co.sparse_singer_data.index[query_index])
	    else:
		if algo=='brute':		
			print '{0}: {1}, with distance of {2}:'.format(i, co.sparse_singer_data.index[indices.flatten()[i]], distances.flatten()[i])
		else:
			print '{0}: {1}, with distance of {2}:'.format(i, co.sparse_singer_data.index[indices.flatten()[i]], 1-(1/(1+distances.flatten()[i]))) 


recommend('brute','cosine',co.sparse_singer_data_compress)
recommend('kd_tree','euclidean',co.sparse_singer_data)

print '\n'