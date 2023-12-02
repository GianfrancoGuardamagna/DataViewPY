import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Columns are altitude, date_time, device_info_serial, direction, latitude, longitude, speed_2d, bird_name
df = pd.read_csv("bird_migration.csv")

# Convertir la columna date_time a tipo datetime
df["date_time"] = pd.to_datetime(df["date_time"])

# Filtrar las fechas y altitudes para el ave Eric
eric_dates = df[df["bird_name"] == "Sanne"]

# Agrupar por mes y calcular el promedio de altitud para cada mes
eric_monthly_avg = eric_dates.groupby(eric_dates["date_time"].dt.to_period("M"))["altitude"].mean()

# Convertir a un DataFrame para facilitar la visualización
eric_monthly_avg_df = eric_monthly_avg.reset_index()

# Crear el gráfico de barras para el promedio mensual de altitud
plt.figure(figsize=(12, 6))
plt.bar(eric_monthly_avg_df["date_time"].astype(str), eric_monthly_avg_df["altitude"], color='b')

#plt.plot(eric_monthly_avg_df["date_time"].astype(str), eric_monthly_avg_df["altitude"], marker='o', linestyle='-', color='r')

# Configurar etiquetas y título
plt.xlabel('Mes')
plt.ylabel('Promedio de Altitud')
plt.title('Promedio Mensual de Altitud de Sanne')
plt.xticks(rotation=45, ha="right")

# Mostrar el gráfico
plt.tight_layout()
plt.show()
