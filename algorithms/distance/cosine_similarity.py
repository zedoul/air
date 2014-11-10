from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
a = np.matrix('1 1 1 1 1 1 1 1 1')
b = np.matrix('1 1 1 0 1 1 1 1 0')
print("cosine_similarity(a,b) %f" %( cosine_similarity(a,b)))
