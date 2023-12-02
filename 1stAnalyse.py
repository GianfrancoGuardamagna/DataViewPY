import pandas as pd
import numpy as np

#Columns are altitude, date_time, device_info_serial, direction, latitude, longitude, speed_2d, bird_name

df = pd.read_csv("bird_migration.csv")

df["date_time"] = pd.to_datetime(df["date_time"])

eric_dates = df[(df["bird_name"]=="Eric")]#ID851
nico_dates = df[(df["bird_name"]=="Nico")]#ID864
sanne_dates = df[(df["bird_name"]=="Sanne")]#ID833

eric_day = eric_dates[(df["date_time"]>="2013-08-15")&(df["date_time"] < "2013-08-16")]

eric_altitude = eric_day["altitude"] # min = -342,max = 476,mean = 74.98809523809524

eric_array = eric_altitude.values

eric_mean = np.mean(eric_array)

print(eric_mean)