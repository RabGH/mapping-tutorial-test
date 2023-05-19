
#TODO Creating a function for map elevation colors
#! Styling the markers with CircleMarker instead of folium.Marker, icon=folium.Marker(color=
#! We have to give the circlemarker a radius (base 10), and a fill_color, color, and opacity parameter
#! We add the color = 'grey' if the markers are blank 
#! the fill_color parameter method in CircleMarker is iterating through the for loop and function color producer
import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation): # We need to call the function before the expression 
    if elevation < 1000: # So el that is passed in the child will pass the integers through this function
        return 'green' # if elevation less that 1000
    elif 1000 <= elevation < 3000: 
        return 'orange' # if elevation less or equal to 1000 but less than 3000
    else:
        return 'red' # if non are satisfied, which means anything over 3000
    # to find the catagory threshold, just look through the text file

map = folium.Map(location = [38.58, -99.08], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat,lon,elev): # So for el here we pass through the function color producer
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=str(el)+" m", fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))
    
map.add_child(fg)
map.save("Map3_dynamin_colors.html")