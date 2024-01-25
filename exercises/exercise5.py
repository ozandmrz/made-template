import urllib.request
import zipfile
import pandas as pd
import sqlite3
import sqlalchemy

url_ = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
def automated_data_pipeline():
    
    ref,message=urllib.request.urlretrieve(url_)

    with zipfile.ZipFile(ref, 'r') as file:
        file.extract('stops.txt')

    df = pd.read_csv('stops.txt', sep=',', header=0, encoding='UTF-8', dtype={ 'stop_id': int, 'stop_name': str, 'stop_lat': float, 'stop_lon': float, 'zone_id': int }, usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id'])

    
    
    df = df[df["zone_id"] == 2001]
    df = df[(-90 <= df["stop_lat"]) & (df["stop_lat"] <= 90)]
    df = df[(-90 <= df["stop_lon"]) & (df["stop_lon"] <= 90)]   
    df.dropna(inplace=True)
    types_={
        "stop_id": sqlalchemy.types.BIGINT,   
        "stop_name": sqlalchemy.types.TEXT,      
        "stop_lat": sqlalchemy.types.FLOAT,      
        "stop_lon": sqlalchemy.types.FLOAT,      
        "zone_id": sqlalchemy.types.BIGINT  }
    
    engine = sqlalchemy.create_engine("sqlite:///gtfs.sqlite")
    
    df.to_sql("stops", engine, if_exists="replace", index=False, dtype=types_)

if __name__ == "__main__":
    automated_data_pipeline()