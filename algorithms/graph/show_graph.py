print(__doc__)
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

W = np.matrix([
[0,0.8,0.6,0,0.1,0],
[0.8,0,0.8,0,0,0],
[0.6,0.8,0,0.2,0,0],
[0,0,0.2,0,0.8,0.7],
[0.1,0,0,0.8,0,0.8],
[0,0,0,0.7,0.8,0],
])


