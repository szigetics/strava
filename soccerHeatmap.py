import matplotlib.pyplot as plt
import gmplot
import gpxpy
import sys

if __name__ == "__main__":

    filename = sys.argv[1]
    path = 'activities/'+filename
    name = filename.split('.')[0]
    lat = []
    lon = []

    gpx_file = open(path, 'r')
    gpx = gpxpy.parse(gpx_file)

    #parsing latitude and longitude
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)

    #generating the trace figure
    fig = plt.figure(facecolor = '0.1')
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_aspect('equal')
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.plot(lon, lat, color = 'deepskyblue', lw = 0.3, alpha = 0.9)
    plt.savefig("plots/"+name+".png", dpi=600)


    #generating the heatmap
    gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 20)
    gmap.heatmap(lat, lon)

    gmap.apikey = "insert your key here"

    gmap.draw("heatmaps/"+name+".html")
