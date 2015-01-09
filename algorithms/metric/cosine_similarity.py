from sklearn.metrics.pairwise import cosine_similarity
i1mport numpy as np
a = np.matrix('1 1 1 1 1 1 1 1 1')
b = np.matrix('1 1 1 0 1 1 1 1 0')
print("cosine_similarity(a,b) %f" %( cosine_similarity(a,b)))

a = np.matrix('1 1')
b = np.matrix('1 0')
print("cosine_similarity(a,b) %f" %( cosine_similarity(a,b)))

a = np.matrix('3 3')
b = np.matrix('1 0')
print("cosine_similarity(a,b) %f" %( cosine_similarity(a,b)))
