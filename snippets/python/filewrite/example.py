#!/usr/bin/env python
a = ["1","2","3"] #range(1,10)

f = open('myfile_1.txt','w')
f.write('1,2,3\n')
f.close()

with open('myfile_2.txt', 'w') as the_file:
    for i in a :
        the_file.write("%s " % i)
