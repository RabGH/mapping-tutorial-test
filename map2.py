
#TODO Using a text file with values about volcanoes and setting up markers for each site 
#! We will read the text file, get it's values, and plug them into the for loops 
#! ID number of the valcano, Number, name, location, status, elevation, type, timeframe, latitude, and longitute
#! We have 10 columns to run through, 62 rows, 63 with the header
#! data["LON"] is a series object 
#! list(data["LON"]) is a python list object
#! We find the columns by using data.columns (data being the variable holding the read text script)
#! We want to plug the LAT and LON columns to the for loop
#! We have to becareful on how we iterate through these 2 lists 
#! We have 2 list, each of them have 62 items. len(lat) len(lon)
#! The first item of the lat list, cooresponds to the second of the lon list
#! The first 2 items make up the first location of the first marker
#! So we need to exract both locations
#! zip function example, for i, j in zip([1,2,3], [4,5,6])
#! print ( i, "and", j), distributes the items 1 by 1 
#! Dynamin popups, we create another variable that will hold all the elevation numbers from the elev column
#! We turn it into a python list, then add it to the for loop zip, by adding an extra variable and naming the variable you made the list in
#! elev = .... is the list variable creates, for el in zip(...elev)
#! An error occurs on the course, while this did not 
#! The error is that popup requires only strings as an argument not floats or integers
#! Elev is a float64 numpy value. To fix this error we add
#! popup=folium.Popup(str(el),parse_html=True)
#TODO Show the map elevation color arrangement 
#! We can catagorize green orange and red, each marker will have a color depending on the number of elevation
#TODO ADDED EVERYTHING FROM ALL OTHER LECTURES INTO THIS ONE + Some personal touches



import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
Type = list(data["TYPE"])
time = list(data["TIMEFRAME"])
status = list(data["STATUS"])

# this is an HTML code that is given to the variable HTML, this allows for a google search of the specific volcano

html = """ 
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
Type: %s
Time Frame: %s
Status: %s
"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
    
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, name, Type, time, status in zip(lat, lon, elev, name, Type, time, status): # When you iterate through 2 lists, you need to use the zip function
    iframe = folium.IFrame(html=html % (name, name, el, Type, time, status), width=200, height=100) # This is the new line added which adds the information for the popup window of the markers
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=folium.Popup(iframe), 
    fill_color = color_producer(el), color = 'grey', color_radius = 0.1 , color_opacity = 0.8))

fgp = folium.FeatureGroup(name = "Population")
    
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x ['properties']['POP2005'] < 10000000
else 'yellow' if 10000000 <= x ['properties']['POP2005'] < 20000000 
else 'orange' if 20000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))
    
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map2.html")

    