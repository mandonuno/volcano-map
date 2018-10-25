#!/usr/bin/env python3
"""Program that creates a map of Volcanoes around the World"""

import folium
import pandas

data = pandas.read_csv("world_volcano.csv")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])
country= list(data["COUNTRY"])

html = """
Name: %s
<br><br>
Height: %s m
<br><br>
Country: %s
"""


def elevation_color(elevation):
    """Function that filters Volcanoes elevation by colors"""

    if elevation < 1000:
        return 'lightblue'
    elif elevation > 1000 and elevation < 3000:
        return 'blue'
    else:
        return 'green'


map = folium.Map(location=[34.501954, -40.963814],
                 zoom_start=2, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Volcanoe Map")

for lt, ln, el, name, country in zip(lat, lon, elev, name, country):
    iframe = folium.IFrame(html=html % (name, el, country), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln],
                               popup=folium.Popup(iframe),
                               icon=folium.Icon(color=elevation_color(el))))

map.add_child(fg)

map.save("Map.html")
