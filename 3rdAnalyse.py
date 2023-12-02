import pandas as pd
import matplotlib.pyplot as plt

#Columns are altitude, date_time, device_info_serial, direction, latitude, longitude, speed_2d, bird_name

df = pd.read_csv("bird_migration.csv")

df["date_time"] = pd.to_datetime(df["date_time"])

eric_dates = df[(df["bird_name"]=="Eric")]#ID851
nico_dates = df[(df["bird_name"]=="Nico")]#ID864
sanne_dates = df[(df["bird_name"]=="Sanne")]#ID833

eric_date_time = eric_dates["date_time"]

eric_altitude = eric_dates["altitude"]

eric_array_x = eric_date_time.values

eric_array_y = eric_altitude.values

plt.figure(figsize=(10, 6))
plt.plot(eric_date_time, eric_altitude,label="Altitud de Eric", color='r')

plt.xlabel('Fecha')
plt.ylabel('Altitud')
plt.title('Altitud de Eric en función del tiempo')

plt.xticks(rotation=45, ha="right")

plt.show()