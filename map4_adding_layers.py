
#TODO Adding layers to the basemap 
#! In GIS Geographic information systems is refered to as layers
#! We want to add a polygon layer, we have a point layer, line layer, and polygon (Areas) layer
#! We are going to add areas with populations, this will point out the population of that country
#! To add polygons via folium by using folium.geojson method
#! json files start with curly brackets that's like a python dictionary
#! It has keys and values that we will extract and add to the script
#! The attribute is a multi-polygon coordinates, it has coordinates for each country
#! This is how it decides where to put the polygons
#! We will also put a color for the population 
#! We use the folium method geojson to extract polygons, 
#! Then use the open method with the variable data open("file.json")
#! We get an error msg, we need to add an encoding parameter which goes inside the open method
#! Recent version of Folium needs a string instead of a file as data input
#! That is why we add the .read() method to the file that we're encoding 
#! ("world.json", 'r', encoding='utf-8-sig').read
#! We can also add points through GeoJson, we added polygons here, but it can also has lines or points in its attributes
#! Folium will display those features depending of attribute in the Json file\
#! We have the coordiantes attributes with the coordiantes of the lines, where the lines break and turn 
#! We will create colorapleth map which is a map that uses colorings of areas to represent features
#! We will have the polygons in different colors to represent the population of countries
#! We're going to use POP2005, population of world in 2005
#! POP2005 is part of the dictionary, these are a set of properties ( Which is in the json ) and is a value of the properties key

import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation): 
    if elevation < 1000: 
        return 'green' 
    elif 1000 <= elevation < 3000: 
        return 'orange' 
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.08], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat,lon,elev): 
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el)+" m", fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))
    
fg.add_child(folium.GeoJson(data = open("world.json", 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x ['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 
# Set green to fill color if x represents the feature, if the pop2005 attribute of properties of that attribute, is less than 10 mill
# We are using this syntax to add colors to the properties key in the json dictionary. POP2005
# x here represents features, we are access properties through features 
# background : Folium will go through all the features of all of the polygons and check if value of POP2005, is less than 10mill, if it is, it will fillcolor
# This displays the polygon layer on the map, it seperates countries borders    
# By default the color is green, and opacity. 
# We need to access the style function argument
# Need to add another argument to GeoJson
# We can break the lines in python as long as it's in brackets
# the style_function expects a lambda function, normal but they are read in single lines of code
# l = lambda x: x**2, l(5) which returns 5 in the power of 2
# This also allows us to write anonymous functions
# In this example, we don't need to call it later, so we don't have to give it a name or variable
map.add_child(fg)
map.save("Map4_Adding_Layers.html")