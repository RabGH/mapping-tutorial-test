# Refer to summary notes!
#! We are to going to add points to the map
#! Creating a new layer over the base map
#! Layer coming from open street service
#! Folium serves the layer through javascript
#! help(folium.map) we can add other things such as
#! Paramter = tiles, we have to put in the map box as a string format
#! Stamen Terrain is a mapbox that adds terrain visuals to the map, we have a new base map now
#! Between the map object and the save method 
#! We can add elements, objects to that map 
#! A marker for example 

import folium 
map = folium.Map(location=[38.58, -99.09], start_zoom=6, tiles="Stamen Terrain")
# Better way to add features to the map 
fg = folium.FeatureGroup(name="My Map") # We can add multiple features to the feature group, marker, polygons, and so on
for coordinates in [[38.2,-99.1],[39.2,-97.1]]: # This a for loop. for coordinates inside of these coordiantes
    fg.add_child(folium.Marker(location=coordinates, popup="Yo I'm a Maker", icon=folium.Icon(color='green'))) # We use the @ child method to add children, objects 
    # Inside of location we changed it to the for loop variable coordinates, so it adds a marker to any coordinates we add into the loop 
    # This reiterates that list of coordinates, instead of having to copy paste it multiple times, it allows for less fat or code 
# It is not possible to add multiple markers with one single method, you need to apply the method multiple times 
# Not very smart to do, we can use a for loop 
# We then add the child or children, which are features in the fg group, to the map
# Keeps more organized, and to add control layer 
# We can add more markers by just re applying the add_child code
# Lets say you have a 1000 coordinates that needs to be mapped
# You can't, for example, paste them from the document into the loop (While you can), it might be froma comma seperated text file and so on
# and you want to load that file into python and load those values into the for loop 
map.add_child(fg)
# excepts arguments, leaflet is javascript to help visualize it 
# Markers allow you to put up pop ups, to show information
# Location parameter to visualize it
# We added a location, a popup which puts up a message, the type of icon and it's color
# marker is a feature 
map.save("Map1.html")