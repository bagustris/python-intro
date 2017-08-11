import time
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import pylab as plb

#   set up figure for plotting:
fig = plt.figure()
ax = fig.add_subplot(111)

#    plot limits
ax.set_xlim(-(max(q0) + bodies[-1].L), +(max(q0) + bodies[-1].L))
ax.set_ylim(-(max(q0) + bodies[-1].L), +(max(q0) + bodies[-1].L))

#    colors
colors = ['b', 'g', 'c']


for i_t in range(np.shape(t)[1]):    #t is an one column matrix
    for i in range(N):
        ax.clear()
        ax.plot(x_matrix[i_t, i], y_matrix[i_t, i], 's', color=colors[i])
        plt.pause(0.001)
        
plt.show()
