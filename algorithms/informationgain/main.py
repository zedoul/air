import csv as csv
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib.mlab as mlab
import math

def load_data(filename):
    csv_file_object = csv.reader(open(filename, 'r'))       # Load in the csv file
    header = csv_file_object.next()                             # Skip the fist line as it is a header
    data=[]                                                     # Create a variable to hold the data
    for row in csv_file_object:                 # Skip through each row in the csv file
        data.append(row)                        # adding each row to the data variable
    data = np.array(data)                       # Then convert from a list to an array
    return data

def entropy(onboard):
    l = len(onboard)
    s = np.sum(onboard)
    n = l - s
    return -1 * s/float(l) * math.log(s/float(l)) -1 * n/float(l) * math.log(n/float(l))

def information_gain(onboard1,onboard2):
    return len(onboard1)*entropy(onboard1) + len(onboard2)*entropy(onboard2)

data = load_data('train.csv')

male_descriptor = data[0::,4] == 'male'
female_descriptor = data[0::,4] != 'male'
class_1_descriptor = data[0::,2] == '1'
class_lower_descriptor = data[0::,2] != '1'
age_older_descriptor = data[ data[0::,5] != '', 5].astype(np.float) > 18 
age_younger_descriptor = data[ data[0::,5] != '', 5].astype(np.float) <= 18

male_onboard = data[male_descriptor,1].astype(np.float)
female_onboard = data[female_descriptor,1].astype(np.float)
class_1_onboard = data[class_1_descriptor,1].astype(np.float)
class_lower_onboard = data[class_lower_descriptor,1].astype(np.float)

data2 = data[ data[0::,5] != '', 1].astype(np.int)
age_older_onboard = data2[age_older_descriptor]
age_younger_onboard = data2[age_younger_descriptor]

proportion_male_survived = np.sum(male_onboard) / np.size(male_onboard)
proportion_female_survived = np.sum(female_onboard) / np.size(female_onboard)
proportion_class_1_survived = np.sum(class_1_onboard) / np.size(class_1_onboard)
proportion_class_lower_survived = np.sum(class_lower_onboard) / np.size(class_lower_onboard)
proportion_age_older_survived = np.sum(age_older_onboard) / float(np.size(age_older_onboard))
proportion_age_younger_survived = np.sum(age_younger_onboard) / float(np.size(age_younger_onboard))

print proportion_male_survived
print proportion_female_survived
print proportion_class_1_survived
print proportion_class_lower_survived
print proportion_age_older_survived
print proportion_age_younger_survived

print "ent - gender"
print entropy(male_onboard)
print entropy(female_onboard)
print information_gain(male_onboard,female_onboard)

print "ent - class"
print entropy(class_1_onboard)
print entropy(class_lower_onboard)
print information_gain(class_1_onboard,class_lower_onboard)

print "ent - age"
print entropy(age_older_onboard)
print entropy(age_younger_onboard)
print information_gain(age_older_onboard,age_younger_onboard)

