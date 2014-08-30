# The first thing to do is to import the relevant packages
# that I will need for my script, 
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call 
# csv.[function] or np.[function] first

import csv as csv 
import numpy as np

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('./train.csv', 'rb')) 
header = csv_file_object.next()  # The next() command just skips the 
                                 # first line which is a header
data=[]                          # Create a variable called 'data'.
for row in csv_file_object:      # Run through each row in the csv file,
    data.append(row)             # adding each row to the data variable
data = np.array(data)            # Then convert from a list to an array
                                 # Be aware that each item is currently
                                 # a string in this format

print data

print data[0:15,5]
print type(data[0::,5])

import pandas as pd
# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('train.csv', header=0)
print df

print df.head(3)

print type(df)
print df.dtypes
print df.describe()
