
import os
import json
import folium
from folium.plugins import MarkerCluster
import numpy as np



with open('inv1Result.json') as json_data:
    d = json.load(json_data)
print(d[0]['inv'])

m = folium.Map(
    #location=[np.mean(lats), np.mean(lons)],
    location = [20,0],
    tiles='Cartodb Positron',
    zoom_start=2
)

marker_cluster = MarkerCluster(
    name='1000 clustered icons',
    overlay=True,
    control=False,
    icon_create_function=None
)

c = len(d)/50
print ("count total: ", len(d))
print ("count shown: ", c)

for i in range(c):
    if (isinstance(d[i]['lat'], float) and isinstance(d[i]['long'], float)):
        print (d[i]['lat'], d[i]['long'])
        ic = folium.features.CustomIcon('C:/Users/mojta/Desktop/optimizedcode/bt.png', icon_size=(20,20))
        marker = folium.Marker([d[i]['lat'],d[i]['long']],icon=ic)
        popup=d[i]['ip']
        folium.Popup(popup).add_to(marker)
        marker_cluster.add_child(marker)
    else:
        print("non float value")

marker_cluster.add_to(m)
folium.LayerControl().add_to(m)

m.save(os.path.join('results', 'bubblemap.html'))


print ("count total: ", len(d))
print ("count shown: ", c)
