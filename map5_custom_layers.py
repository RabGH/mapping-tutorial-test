
#TODO Implmenting a feature which allows to turn the custom layers on and off
#! Polygon layer and circle point layer, and the base layer 
#! Key feature is layer control class of the folium module
#! When adding folium.LayerControl() and run it, it will only show the base map 
#! Nothing else at all, reason is: when we added layercontrol and it can't find the featuregroups
#! Needs to be after we've added the feature group 
#! Having layer control only lets you on and off both layers
#! Polygon layer and point layer, needs to be seperated
#! Better to add it all to a featuregroup, or it would be one layer per volcano point, if it was done with map.add_child instead of fg


import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data["LON"])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes") # Has to be before the FeatreGroup added with a specific name for readability 

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup=str(el)+" m", 
    fill_color= color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population") 

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x ['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv) # Layer control will only see this as one single object, it contains both
map.add_child(fgp)

map.add_child(folium.LayerControl()) 

map.save("Map5_custom_layers.html")