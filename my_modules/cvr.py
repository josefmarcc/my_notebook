import requests
import pandas as pd
import numpy as np 
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import csv, json

class NotFoundException(Exception):
    pass

def download(country_code, CVR):
    apiURL = "https://cvrapi.dk/api?"
    r = requests.get(apiURL, params={'country': country_code, 'search': CVR})


    if r.status_code == 404:
        print("404 Error")
        raise NotFoundException

    filename = "cvr_data/" + str(CVR) + ".xlsx"    

    data = r.text
    df = pd.read_json(data, index=False)
    df.to_excel(df)


def multi_download(CVR_list):
        workers = len(CVR_list)
        
        with ThreadPoolExecutor(workers) as executor:
            executor.map(download, CVR_list, range(len(CVR_list)))




# Lav Dataframe fra CSV
df_semi = pd.read_csv("/home/jovyan/my_notebooks/my_modules/CVR testdata.csv", sep=";")
#print(df_semi)

# Hent på flere 
#for ind in df_semi.index: 
#     download(df_semi['COUNTRY'][ind], df_semi['CVR_NUMMER'][ind])

download('DK', 18609703)