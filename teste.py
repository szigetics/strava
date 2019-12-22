#Soccer Heatmap

import numpy as np
import numpy.random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

x = []
y = []

with open("Evening_Run.tcx") as fp:
    line = fp.readline()

    while line:
        test = line.split(">")[0]
        if test == "<LatitudeDegrees" or test == "       <LatitudeDegrees":
            lat = line.split(">")[1][:10]
            LatitudeDegrees = float(lat)
            #print("latitude: ")
            #print(lat)
            x.append(LatitudeDegrees)

        if test == "<LongitudeDegrees" or test == "       <LongitudeDegrees":
            lon = line.split(">")[1][:10]
            LongitudeDegrees = float(lon)
            #print("longitude: ")
            #print(lon)
            y.append(LongitudeDegrees)

        line = fp.readline()

#--------------------------------------------------------------
# Create heatmap
#heatmap, xedges, yedges = np.histogram2d(x, y, bins=(20,20))
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Plot heatmap
#plt.clf()
#plt.title('First heatmap example')
#plt.ylabel('y')
#plt.xlabel('x')
#plt.imshow(heatmap, extent=extent)
#plt.show()
#-------------------------------------------------------------

#Create figure
fig=plt.figure()
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)

#Pitch Outline & Centre Line
plt.plot([0,0],[0,90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")
plt.plot([65,65],[0,90], color="black")

#Left Penalty Area
plt.plot([16.5,16.5],[65,25],color="black")
plt.plot([0,16.5],[65,65],color="black")
plt.plot([16.5,0],[25,25],color="black")

#Right Penalty Area
plt.plot([130,113.5],[65,65],color="black")
plt.plot([113.5,113.5],[65,25],color="black")
plt.plot([113.5,130],[25,25],color="black")

#Left 6-yard Box
plt.plot([0,5.5],[54,54],color="black")
plt.plot([5.5,5.5],[54,36],color="black")
plt.plot([5.5,0.5],[36,36],color="black")

#Right 6-yard Box
plt.plot([130,124.5],[54,54],color="black")
plt.plot([124.5,124.5],[54,36],color="black")
plt.plot([124.5,130],[36,36],color="black")

#Prepare Circles
centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
centreSpot = plt.Circle((65,45),0.8,color="black")
leftPenSpot = plt.Circle((11,45),0.8,color="black")
rightPenSpot = plt.Circle((119,45),0.8,color="black")

#Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

#Prepare Arcs
leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

#Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)

#Tidy Axes
plt.axis('off')

sns.kdeplot(x,y, shade=True,n_levels=50)
plt.ylim(0, 90)
plt.xlim(0, 130)


#Display Pitch
plt.show()
