import csv
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

hFile = open("Location.csv", 'r')
sFile = open("Sensor.csv", 'r')
datfile = csv.reader(hFile)
satfile = csv.reader(sFile)
dat = []
sat = []

for row in datfile:
        dat.append(map(float,row))

for row in satfile:
        sat.append(map(float,row))

temp = zip(*(dat))
sense = zip(*(sat))

fig = pylab.figure(figsize=pyplot.figaspect(.96))
#Trajectory
ax = Axes3D(fig)
ax.axis([-5,5,-5,5])
ax.plot_wireframe(temp[0], temp[1], temp[2])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
pylab.savefig('Trajectory')
pos = pyplot.figure()
pos.suptitle('Position')
pyplot.xlabel('Time(Secs)')
pyplot.ylabel('Distance')
# Position in space with Time
X, = pyplot.plot(temp[7], temp[0])#, label = 'X')
Y, = pyplot.plot(temp[7], temp[1])#, label = 'Y')
Z, = pyplot.plot(temp[7], temp[2])#, label = 'Z')
pyplot.legend([X,Y,Z],['X','Y','Z'])
pyplot.savefig('Position')
quat = pyplot.figure()
pyplot.ylim([-0.5,1.5])
quat.suptitle('Quaternions')
pyplot.xlabel('Time(Secs)')
# Quaternions with time
W, = pyplot.plot(temp[7], temp[3])#, label = 'X')
A, = pyplot.plot(temp[7], temp[4])#, label = 'Y')
B, = pyplot.plot(temp[7], temp[5])#, label = 'Z')
G, = pyplot.plot(temp[7], temp[6])#, label = 'Z')
pyplot.legend([W,A,B,G],['X','Y','Z','W'])
pyplot.savefig('Quaternion')
la = pyplot.figure()
la.suptitle('Linear Acceleration')
pyplot.xlabel('Time(Secs)')
pyplot.ylabel('Acceleration')
#Linear Acceleration with time
AL, = pyplot.plot(sense[6], sense[0])#, label = 'X')
BE, = pyplot.plot(sense[6], sense[1])#, label = 'Y')
GA, = pyplot.plot(sense[6], sense[2])#, label = 'Z')
pyplot.legend([AL,BE,GA],['X','Y','Z'])
pyplot.savefig('Acceleration')
av = pyplot.figure()
av.suptitle('Angular Velocity')
pyplot.xlabel('Time(Secs)')
pyplot.ylabel('Angular Velocity')
#Angular Velocity with time
A1, = pyplot.plot(sense[6], sense[3])#, label = 'X')
B1, = pyplot.plot(sense[6], sense[4])#, label = 'Y')
C1, = pyplot.plot(sense[6], sense[5])#, label = 'Z')
pyplot.legend([A1,B1,C1],['X','Y','Z'])
pyplot.savefig('Velocity')
pyplot.show()

