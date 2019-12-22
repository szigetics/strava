#Soccer Heatmap

#import numpy as np
#import numpy.random
#import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
#from matplotlib.patches import Arc

import gpxpy
import gmplot

if __name__ == "__main__":

    lat = []
    lon = []

    gpx_file = open('Evening_Run.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)


    fig = plt.figure(facecolor = '0.1')
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_aspect('equal')
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.plot(lon, lat, color = 'deepskyblue', lw = 0.3, alpha = 0.9)
    plt.savefig("outputs/trace.png", dpi=600)
    plt.savefig("outputs/trace.pdf", dpi=600)

    gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 20)

    gmap.heatmap(lat, lon)
    gmap.draw("outputs/heatmap.html")
