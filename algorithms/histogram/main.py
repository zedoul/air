import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib.mlab as mlab

def load_data(filename):
    csv_file_object = csv.reader(open(filename, 'r'))       # Load in the csv file
    header = csv_file_object.next()                             # Skip the fist line as it is a header
    data=[]                                                     # Create a variable to hold the data
    for row in csv_file_object:                 # Skip through each row in the csv file
        data.append(row)                        # adding each row to the data variable
    data = np.array(data)                       # Then convert from a list to an array
    return data

def save_histogram(data, title, number_of_bins, rng, filename):
    mu = np.mean(data)
    sigma = np.var(data)
    n, bins, patches = plt.hist(data, number_of_bins, rng, histtype='bar', normed=True, facecolor='green')
    y = mlab.normpdf(bins, mu, sigma)
    plt.title(title, bbox={'facecolor':'0.8', 'pad':5})
    plt.plot(bins, y, 'r--', linewidth=1.5)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

data = load_data('train.csv')
save_histogram(map(int,data[0::,1]), 'survived', 2, (0, 1), 'survived.png')
save_histogram(map(int,data[0::,2]), 'class', 3, (1, 3), 'class.png')
save_histogram([int(i!='male') for i in data[0::,4]], 'gender', 2, (0, 1), 'gender.png')

print data[0::,9]
d = map(float,data[0::,9])
print min(d)
print max(d)
save_histogram(d, 'fare', 5, (min(d), max(d)), 'fare.png')

