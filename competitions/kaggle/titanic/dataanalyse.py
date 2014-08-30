import pylab

# make a square figure and axes
pylab.figure(1, figsize=(6,6))
ax = pylab.axes([0.1, 0.1, 0.8, 0.8])
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]
explode=(0, 0.05, 0, 0)
pylab.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
pylab.title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

pylab.savefig('mean.png')
