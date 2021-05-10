import folium

#Edinburgh
a = 55.94
b = -3.19
#Allonby
aa = 54.77
ab = -3.42
#Isle of Wight
ba = 50.69
bb = -1.30
#Orlando Florida
ca = 28.53
cb = -81.37
#Paris
da = 48.85
db = 2.35
#Ibiza
ea = 39.02
eb = 1.48
#Majorca
fa = 39.69
fb = 3.01
#Tenerife
ga = 28.29
gb = -16.62
#eygpt
ha = 27.96
hb = 34.36
#phuket
ia = 7.88
ib = 98.39


map =folium.Map(location=[a, b], zoom_start=4,)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[a, b], popup="Edinburgh", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[aa, ab], popup="Allonby", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ba, bb], popup="Isle of Wight", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ca, cb], popup="Orlando", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[da, db], popup="Paris", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ea, eb], popup="Ibiza", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[fa, fb], popup="Majorca", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ga, gb], popup="Tenerife", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ha, hb], popup="Eygpt", icon=folium.Icon(color='green')))
map.add_child(fg)
fg.add_child(folium.Marker(location=[ia, ib], popup="Phuket", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("HolidayLocations.html")

# The above created the Map Html with the co-ordinates (long&Lat) and sets the Zoom status on the Map, it also addes a marker to the map, this is ok for one marker but adding mutiple marks can be problematic.
