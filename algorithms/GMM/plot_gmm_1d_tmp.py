import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.colors import LogNorm
from sklearn import mixture

#def make_ellipses(gmm, ax):
#    for n, color in enumerate('rgb'):
#        v, w = np.linalg.eigh(gmm._get_covars()[n][:2, :2])
#        u = w[0] / np.linalg.norm(w[0])
#        angle = np.arctan2(u[1], u[0])
#
#        angle = 180 * angle / np.pi  # convert to degrees
#        v *= 9
#        ell = mpl.patches.Ellipse(gmm.means_[n, :2], v[0], v[1],
#                                  180 + angle, color=color)
#        ell.set_clip_box(ax.bbox)
#        ell.set_alpha(0.5)
#        ax.add_artist(ell)

def gd(x,mean,variance):
    sigma = np.sqrt(variance)
    return mlab.normpdf(x,mean,sigma)

x = np.linspace(-10,10,100)
y1 = gd(x,0,1)
y2 = gd(x,5,0.4)
y3 = gd(x,-4,2)

plt.plot(x,y1+y2+y3)

clf = mixture.GMM(n_components=2, covariance_type='full')
clf.fit(x)


h = plt.subplot(2, 4 / 2, 0 + 1)
classifier = clf 
make_ellipses(classifier, h)

plt.show()
