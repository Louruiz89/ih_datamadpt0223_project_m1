<p align="left"><img src="https://pbs.twimg.com/media/EQimOZYXkAMCZfv?format=jpg&name=small"></p>

# BiciMAD Stations <-> Embassies

<p align="left"><img src="https://brandemia.org/contenido/subidas/2023/01/bicimad-logo-e-identidad-2023.png"></p>

## **Status:**

Ironhack Madrid - Data Analytics Part Time - Feb 2023 - Project Module 1

## **My Project:**

In this project we need to generate a CSV file with the nearest BiciMAD Station to a Place of interest of Madrid. In __my project__, I need to show the nearest BiciMAD Station to the embassies located in Madrid.

## **DDBB:**

Information collected by 2 points:

1. BBDD 
con = duckdb.connect("../data/bicimad.db",read_only=True)
df_bicis = con.sql("SELECT * FROM bicimad_stations").df()

2. API
endpoint = 'https://datos.madrid.es/egob'
lourdes = '/catalogo/201000-0-embajadas-consulados.json'
response = requests.get(endpoint + lourdes)

## **Technology stack:**

Languaje: Python

Tools: Jupyter Notebook and Visual Studio Code

Imports: 
import geopandas
import duckdb
import pandas as pd
import requests
import json
import re
from shapely.geometry import Point
import argpars


**The project must meet the following requirements:**

- It must be contained in a GitHub repository which includes a README file that explains the aim and content of your code. You may follow the structure suggested [here](https://github.com/potacho/data-project-template).

- It must create, at least, a `.csv` file including the requested table (i.e. Main Challenge). Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 

- It must provide, at least, two options for the final user to select when executing using `argparse`: **(1)** To get the table for every 'Place of interest' included in the dataset (or a set of them), **(2)** To get the table for a specific 'Place of interest' imputed by the user.





 


 

