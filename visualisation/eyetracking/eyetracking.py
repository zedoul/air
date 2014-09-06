#!/usr/bin/env python
from sklearn.ensemble import RandomForestClassifier
import csv_io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

training, target = csv_io.read_data("./test.csv")
d = training[10]
lx = d[:2048]
ly = d[2048:2048*2]
rx = d[2048*2:2048*3]
ry = d[2048*3:]

def data_gen():
    cnt = -1
    while cnt < 2047:
        cnt+=1
        yield lx[cnt], ly[cnt]
    print "Finished"

data_gen.t = 0
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-600, 200)
ax.set_xlim(0, 800)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    t,y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    line.set_data(xdata, ydata)
    return line,

def main():
    ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10, repeat=False)
    plt.show()

if __name__=="__main__":
    main()
