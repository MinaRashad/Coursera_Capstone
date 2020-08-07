import numpy as np
import pandas as pd
import requests
import json
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import date
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
import matplotlib.cm as cm
import matplotlib.colors as colors
import folium # map rendering library

URL = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
#Getting the data
rawDataRES = requests.get(URL)
rawData = rawDataRES.text
#Removing unimportant Parts
rawData =rawData.split("<table class=\"wikitable sortable\">\n<tbody>")[1]
rawData = rawData.split("</tbody></table>")[0]
rawData = rawData[79:]
rawData = rawData.replace("<td>","")
rawData = rawData.replace(",","~")
rawData = rawData.replace("\n</td>\n",",")
rawData = rawData.replace("\n</td></tr>\n<tr>","")
rawData = rawData.replace("\n</td></tr>","")


columnNames = ["PostalCode","Borough","Neighborhood"]
df = pd.DataFrame(columns=columnNames)

for entry in rawData.splitlines():
    entry = entry.split(",")
    code = entry[0]
    borough = entry[1]
    neighbours = entry[2]
    if borough == "Not assigned":
        continue
    if neighbours == "Not assigned":
        neighbours = borough
    elif len(neighbours.split("~")) >1:
        neighbours = neighbours.replace("~",",")
    data = {
        "PostalCode":code,
        "Borough":borough,
        "Neighborhood":neighbours
    }
    df = df.append(data,ignore_index=True)

        

print(df.head())
