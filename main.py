#imports
import pandas as pd
import geopandas
import numpy as np
from shapely.geometry import Point

#Call the CSV files
df_bicimad = pd.read_csv('data\clean_bicimad.csv')
df_embajadas = pd.read_csv('data\clean_embajadas.csv')

#Run the function
#transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
def to_mercator(lat, long):
    c = geopandas.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

#Run the function
# return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
def distance_meters(lat_start, long_start, lat_finish, long_finish):
    start = to_mercator(lat_start, long_start)
    finish = to_mercator(lat_finish, long_finish)
    return start.distance(finish)
#Run the function
# return the distance in metres between to latitude/longitude pair point in degrees (i.e.: 40.392436 / -3.6994487)
distance_total = []
for idx, rows_e in df_embajadas.iterrows():
    for idx, rows_b in df_bicimad.iterrows():
        distance_total.append(distance_meters(rows_e['embajada_latitude'],rows_e['embajadas_longitude'],rows_b['lat_bici'],rows_b['long_bici']))
print(distance_total)

distance_total = np.array(distance_total).reshape(len(df_embajadas), len(df_bicimad))

min_indexes = np.argmin(distance_total, axis=1)
df_embajadas['min_distance'] = np.min(distance_total, axis=1)
df_embajadas['closest_station'] = df_bicimad.iloc[min_indexes]['BiciMAD station'].reset_index(drop=True)

df_bicimad_embajadas = df_embajadas[["Place of interest","Type of place","address","closest_station"]]

df_bicimad_embajadas.rename(columns = {'closest_station':'BiciMAD station'}, inplace = True)

df_bicimad_stations = df_bicimad[["BiciMAD station","Station location"]]

final_df = pd.merge(df_bicimad_embajadas, df_bicimad_stations, on='BiciMAD station')
final_df.rename(columns = {'address':'Place address'}, inplace = True)

print(final_df[:5])
