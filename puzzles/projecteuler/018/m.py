def problem(data_file):
    # a list to represent the triangle
    triangle = []
    # read the data file
    # for each line in the data file, append a row (list) to the triangle
    for line in data_file:
        row = [int(i) for i in line.split(" ")] # convert the line to a list
        triangle.append(row)
    
    # for each cell in the triangle, add the max of the cells below-left and
    # below-right. the cell at the top will contain the greatest sum from bottom
    # to top
    for i in range(len(triangle)-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] += max([triangle[i+1][j],triangle[i+1][j+1]])
    return triangle[0][0]

import time
p018_data_file = open("p018_triangle.txt", "r")
p067_data_file = open("p067_triangle.txt", "r")

start = time.clock()
ret = problem(p018_data_file)
elapsed = time.clock() - start
print "p018_maximum path cost: %d" % (ret)
print "found %d in %s seconds" % (ret,elapsed)

start = time.clock()
ret = problem(p067_data_file)
elapsed = time.clock() - start
print "p067_maximum path cost: %d" % (ret)
print "found %d in %s seconds" % (ret,elapsed)
