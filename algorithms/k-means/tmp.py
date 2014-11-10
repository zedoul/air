# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

k = 3;
est = KMeans(n_clusters=k)

X = np.array([
[0,0,1,0], 
[0,0,2,0], 
[0,0,3,0],
[1,0,0,0],
[2,0,0,0],
[3,0,0,0],
[0,0,0,1],
[0,0,0,2],
[0,0,0,3],
],np.int32)

fignum = 1
fig = plt.figure(fignum, figsize=(4, 3))
plt.clf()

ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
est.fit(X)
cluster_centers = est.cluster_centers_
labels = 'asfdsf'
ax.scatter(X[:, 3], X[:, 0], X[:, 2]) #, c=labels.astype(np.float))
cluster_center = cluster_centers[0]
ax.plot(cluster_centers[:,3], cluster_centers[:,0], cluster_centers[:,2], 'x', markerfacecolor='#4EACC5',markeredgecolor='k', markersize=6)

plt.show()
