import pandas
import folium
map = folium.Map(location=[23.379379,79.4433265],zoom_start=5,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="COVID 19")
 
data = pandas.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv")
dateRep = list(data["dateRep"])
cases = list(data["cases"])
deaths = list(data["deaths"])
countriesAndTerritories = list(data["countriesAndTerritories"])
 
data_cor= pandas.read_csv("country.csv")
data_cor1 = data_cor.set_index("name")
 
all_city = []
all_cases = []
all_deaths = []
all_cordi = []
temp_dt = 0
temp_cs = 0
temp_ct = "first_itr"
for dt, cs, dt, ct in zip(dateRep,cases,deaths,countriesAndTerritories):
    if temp_ct == ct:
        temp_dt = temp_dt + dt
        temp_cs = temp_cs + cs
    elif temp_ct != "first_itr":
        all_city .append(temp_ct)
        all_cases.append(temp_cs)
        all_deaths.append(temp_dt)
        temp_ct = ct
        temp_dt = 0
        temp_cs = 0
        temp_dt = temp_dt + dt
        temp_cs = temp_cs + cs
    else:
        temp_ct = ct
        temp_dt = temp_dt + dt
        temp_cs = temp_cs + cs
 
for app_ct, app_cs ,app_dt in zip(all_city,all_cases,all_deaths):
    if app_ct != "Curaçao" and app_ct !="Turks_and_Caicos_islands":
        if float(app_cs) < 15000:
            clr = 'green'
        elif float(app_cs) >= 15000 and float(app_cs) < 50000:
            clr = 'orange'
        else:
            clr = 'red'
        temp_cordi = list(data_cor1.loc[app_ct])
        temp_lat = float(temp_cordi[1])
        temp_lon = float(temp_cordi[2])
        fg.add_child(folium.Marker(location=[temp_lat,temp_lon], popup=str(app_ct)+" \n Cases: " +str(app_cs)+ "\n Deaths : "+str(app_dt),icon=folium.Icon(color=clr)))
 
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("covid.html")