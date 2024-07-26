
import numpy as np 
import pandas as pd 
import os
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
import matplotlib.pyplot as plt
template = "plotly_dark"
plt.style.use('dark_background')
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


#Conjunto de datos EDA
df=pd.read_csv("Electric_Vehicle_Population_Size_History_By_County_.csv")
print(df)

#Crear columnas de año, mes y día
days=list()
months=list()
years=list()
for x in df["Date"]:
    x_split=x.split()
    days.append(x_split[1])
    months.append(x_split[0])
    years.append(x_split[2])
    
df["year"]=years
df["month"]=months
df["day"]=days

#EDA
df.info() #varias columnas están mal clasificadas aquí. Vamos a arreglarlas
df["Battery Electric Vehicles (BEVs)"] = pd.to_numeric(df["Battery Electric Vehicles (BEVs)"].str.replace(",", "").str.replace(".",""), errors='coerce')
df["Plug-In Hybrid Electric Vehicles (PHEVs)"] = pd.to_numeric(df["Plug-In Hybrid Electric Vehicles (PHEVs)"].str.replace(",", "").str.replace(".",""), errors='coerce')
df["Electric Vehicle (EV) Total"] = pd.to_numeric(df["Electric Vehicle (EV) Total"].str.replace(",", "").str.replace(".",""), errors='coerce')
df["Non-Electric Vehicle Total"] = pd.to_numeric(df["Non-Electric Vehicle Total"].str.replace(",", "").str.replace(".",""), errors='coerce')
df["Total Vehicles"] = pd.to_numeric(df["Total Vehicles"].str.replace(",", "").str.replace(".",""), errors='coerce')

#normalmente no sería tan difícil convertir a tipo numérico, pero aquí nuestros datos contienen comas y puntos, por lo que 
# los eliminamos y luego los convertimos a numéricos.

print(df.info())

print(df.describe().T)

#Dondequiera que haya una alta proporción de vehículos eléctricos, hay una buena transición hacia los automóviles eléctricos.
#y veremos estas proporciones de diferentes maneras

#Según los valores del porcentaje de vehículos eléctricos del condado

# Suponiendo que df es su DataFrame que contiene datos sobre vehículos

# Grupo por condado y suma agregada de vehículos eléctricos totales y vehículos totales
df_groupby_county = df.groupby("County").agg({"Electric Vehicle (EV) Total": "sum", "Total Vehicles": "sum"})

# Calcular la proporción de vehículos eléctricos dentro de cada condado
df_groupby_county["Electric Vehicle Ratio"] = df_groupby_county["Electric Vehicle (EV) Total"] / df_groupby_county["Total Vehicles"]

# Mostrar el DataFrame resultante
(df_groupby_county)

df_groupby_county

df_groupby_county["County"]=df_groupby_county.index

df_groupby_county

#Primeros 20 condados con proporción de vehículos eléctricos según el condado
df_groupby_county=df_groupby_county.sort_values(by="Electric Vehicle Ratio", ascending=False)#para ordenar datos
plt.figure(figsize=(12,8))
plt.title("Proporción de los primeros 20 vehículos eléctricos del condado según el condado\n")
plt.xticks(rotation=45)#Devolver x etiquetas para lectura
sns.barplot(df_groupby_county.head(20),x="County",y="Electric Vehicle Ratio", color = "mistyrose", edgecolor = "orangered")

#Ratio de vehículos eléctricos por provincia según año
df_groupby_year = df.groupby("year").agg({"Electric Vehicle (EV) Total": "sum", "Total Vehicles": "sum"})

df_groupby_year["year"]=df_groupby_year.index

print(df_groupby_year)

df_groupby_year["Electric Vehicle (EV) Ratio"]=df_groupby_year["Electric Vehicle (EV) Total"] / df_groupby_year["Total Vehicles"]

print(df_groupby_year)

#para ordenar datos
df_groupby_year=df_groupby_year.sort_values(by="Electric Vehicle (EV) Ratio", ascending=False)
plt.figure(figsize=(12,8))
plt.title("Ratio de vehículos eléctricos por provincia según año\n", fontsize = '16', fontweight = 'bold')
plt.xticks(rotation=45)
sns.barplot(df_groupby_year,x="year",y="Electric Vehicle (EV) Total", color= "pink", edgecolor = "hotpink")

print(df)

#Uso de vehículos eléctricos por año, vehículo
passenger_data = df[df['Vehicle Primary Use'] == 'Passenger']
truck_data = df[df['Vehicle Primary Use'] == 'Truck']

passenger_data=passenger_data.groupby("year").agg({"Electric Vehicle (EV) Total":"sum"})

print(passenger_data)

truck_data=truck_data.groupby("year").agg({"Electric Vehicle (EV) Total":"sum"})

print(truck_data)

sns.lineplot(data=passenger_data, x='year', y='Electric Vehicle (EV) Total', label='Pasajero', marker='o', color='blue')
sns.lineplot(data=truck_data, x='year', y='Electric Vehicle (EV) Total', label='Camión', marker='s', color='fuchsia')
plt.title('Total de vehículos eléctricos (EV) por año y tipo de vehículo\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Año\n')
plt.ylabel('Vehículo eléctrico (EV) Total\n')

# Mostrar gráficos
plt.legend()  # Para mostrar etiquetas de línea
plt.grid(True)  # Para agregar cuadrícula (opcional)
plt.show()

data = pd.read_csv('Electric_Vehicle_Population_Size_History_By_County_.csv')

print(data.sample(4))

print(data.shape)

print('Información de Datos:','\n')
print(data.info(),'\n')

print('Descripción de datos','\n')
data.describe()

data.sample(4)

data['Vehicle Primary Use'] = data['Vehicle Primary Use'].map({'Passenger': 1,'Truck' : 0})

columns_to_convert = ['Electric Vehicle (EV) Total', 'Plug-In Hybrid Electric Vehicles (PHEVs)',
                      'Battery Electric Vehicles (BEVs)', 'Non-Electric Vehicle Total']

# Convertir columnas en cadenas y luego aplicar transformaciones
for col in columns_to_convert:
    data[col] = data[col].astype(str).str.replace(',', '').astype(int)
    
countries_with_EV = data.groupby('County').agg({
    'Electric Vehicle (EV) Total': 'sum',
    'Battery Electric Vehicles (BEVs)': 'sum',
    'Plug-In Hybrid Electric Vehicles (PHEVs)': 'sum',
    'Non-Electric Vehicle Total': 'sum',
    'Percent Electric Vehicles' : 'mean',
    'Vehicle Primary Use': lambda x: x.mode().iloc[0]
}).reset_index() 

print(countries_with_EV)

countries_sorted = countries_with_EV.sort_values(by='Percent Electric Vehicles', ascending=False).head(15)

# Graficado
plt.style.use('dark_background')
plt.figure(figsize=(12, 6))
plt.bar(countries_sorted['County'], countries_sorted['Electric Vehicle (EV) Total'], label='Vehículos eléctricos', color = "fuchsia")
plt.bar(countries_sorted['County'], countries_sorted['Non-Electric Vehicle Total'], bottom=countries_sorted['Electric Vehicle (EV) Total'], label='Vehículos no eléctricos', color = "aqua")
plt.xlabel('Condado\n')
plt.ylabel('Vehículos totales\n')
plt.title('Vehículos eléctricos y no eléctricos por condado\n', fontsize = '16', fontweight = 'bold')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=countries_with_EV, x='Electric Vehicle (EV) Total', y='Percent Electric Vehicles', hue='Vehicle Primary Use', palette='Set2')
plt.xlabel('Total de vehículos eléctricos\n')
plt.ylabel('Porcentaje de vehículos eléctricos\n')
plt.title('Relación entre el total de vehículos eléctricos y el porcentaje de vehículos eléctricos\n', fontsize = '16', fontweight = 'bold')
plt.legend(title='Uso primario del vehículo', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
explode = (0.2, 0.2)
labels = ['Vehículos eléctricos de batería (BEV)', 'Vehículos eléctricos híbridos enchufables (PHEV)']
sizes = [countries_with_EV['Battery Electric Vehicles (BEVs)'].sum(), countries_with_EV['Plug-In Hybrid Electric Vehicles (PHEVs)'].sum()]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors = ["lightpink", "plum"], explode = explode)
plt.title('Distribución de BEV y PHEV\n', fontsize = '16', fontweight = 'bold')
plt.axis('equal')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=countries_sorted, x='County', y='Electric Vehicle (EV) Total', marker='o', color= "violet")
plt.xlabel('Condado\n')
plt.ylabel('Total de vehículos eléctricos\n')
plt.title('Adopción de vehículos eléctricos por condado\n', fontsize = '16', fontweight = 'bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

countries_with_EV.drop(columns=['County'],axis=1,inplace=True)

expected_clustors = range(1,5)
wcss = []
for i in expected_clustors:
    kmeans = KMeans(i)
    kmeans.fit(countries_with_EV)
    wcss.append(kmeans.inertia_)
    
plt.figure(figsize=(14,4))
plt.plot(expected_clustors,wcss, marker='v', color = "crimson")
plt.xlabel('Clústeres\n')
plt.ylabel('WCSS/Inercia\n')
plt.legend()
plt.show()

kmeans2 = KMeans(n_clusters=3)

kmeans2.fit(countries_with_EV)

avg_silhouette_score = silhouette_score(countries_with_EV,kmeans2.labels_)
print('El avg_silhouette_score es ',avg_silhouette_score)
