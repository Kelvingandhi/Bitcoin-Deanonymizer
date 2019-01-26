
import json
import folium
import numpy as np
from types import *
import os


with open('inv1Result.json') as json_data:
    d = json.load(json_data)
print(d[0]['inv'])

m = folium.Map(
    #location=[np.mean(lats), np.mean(lons)],
    location = [20,0],
    tiles='Cartodb Positron',
    zoom_start=2
)
c = len(d)/50
print ("count total: ", len(d))
print ("count shown: ", c)
for i in range(c):
    if (isinstance(d[i]['lat'], float) and isinstance(d[i]['long'], float)):
        print (d[i]['lat'], d[i]['long'])
        ic = folium.features.CustomIcon('C:/Users/mojta/Desktop/optimizedcode/bt.png', icon_size=(20,20))
        folium.Marker([float(d[i]['lat']),float(d[i]['long'])],popup=d[i]['ip'],icon=ic).add_to(m)
    else:
        print("non float value")


m.save(os.path.join('results', 'markermap.html'))


print ("count total: ", len(d))
print ("count shown: ", c)

