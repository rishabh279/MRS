import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd

class plotHeatMap:
    
    def __init__ (self , sparse_singer_data):
        plt.figure(1)
        plt.switch_backend('TkAgg') #TkAgg (instead Qt4Agg)

        bounds = np.array([0, 100, 200, 300, 400, 500,  600, 700, 1000, 2000, 3000, 4000, 5000, 10000, 25000, 500000]) #MRS intervals
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)

        fig = plt.figure()
        
        ax = fig.add_subplot(111)

        cax = ax.matshow(sparse_singer_data, interpolation='nearest',cmap=plt.get_cmap('RdBu_r'), norm=norm)
        cb = fig.colorbar(cax)
        cb.set_label('Number Of Plays')


#        cax.axes.get_xaxis().set_visible(False)
#        cax.axes.get_yaxis().set_visible(False)

        ax.set_xlabel('Users', fontsize=12, color='Blue')
        ax.set_ylabel('Artists', fontsize=12, color='Green')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')

    def show(self):
        
        plt.show();
