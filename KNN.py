from Country import Country as co
import numpy as np
from sklearn.neighbors import NearestNeighbors
from gui import gui as g
from Tkinter import *

# Randomly select artist
#query_index = np.random.choice(co.sparse_singer_data.shape[0])

# Fit filtered data in model
def recommend(algo,dist,inp,query_index):
	
	model_knn = NearestNeighbors(algorithm = algo, metric = dist)
	model_knn.fit(inp)

	# Get nearest neighbours
	distances, indices = model_knn.kneighbors(co.sparse_singer_data.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

	# Display the recommended artists
	abc=''
	for i in range(0, len(distances.flatten())):
	    if i == 0:
		abc += '\n\nRecommendations for {0}:\n\n'.format(co.sparse_singer_data.index[query_index])
	    else:
		if algo=='brute':		
			abc += '{0}: {1}, with distance of {2}\n\n'.format(i, co.sparse_singer_data.index[indices.flatten()[i]], distances.flatten()[i])			
			var.set(abc)
		else:
			#var.set('{0}: {1}, with distance of {2}:'.format(i, wide_artist_data.index[indices.flatten()[i]], 1-(1/(1+distances.flatten()[i])))) 
			var.set(abc)


for item in co.sparse_singer_data.index.values:
    g.listbox.insert(END,item)

frame2 = Frame(g.master, pady=20)
var = StringVar()
label = Message( frame2, textvariable=var, width=500, font="Helvetica 12", pady=-15, padx=20 )
def clickButton():
	if len(g.listbox.curselection())>0 :
		label.config(relief="raised")
		global sel
		sel = g.listbox.curselection()[0]	
		#var.set(str(sel))
		recommend('brute','cosine',co.sparse_singer_data_compress,sel)
		#recommend('kd_tree','euclidean',wide_artist_data,sel)
		
b = Button(g.master, text="Recommend", command=clickButton)
b.pack()
label.pack()
frame2.pack()
mainloop()
print '\n'
