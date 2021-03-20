import json
import requests

import numpy as np
data_array = np.genfromtxt("/home/jovyan/my_notebooks/my_modules/CVR testdata.csv", delimiter=';', dtype=np.uint, skip_header=1)

url = "https://cvrapi.dk/api"
query = {'country': 'DK', 
         'search': '20646411'
}                

r = requests.get(url, params=query)

print(data_array)

print(r.json())