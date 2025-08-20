import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#================================
# 1. Carga de datos 
#================================
df = pd.read_csv(r'd:\Trabajos de la U\Curso IA Mintic\IA_G296\Mision2\Clientes\clientes_supermercado.csv')
print (df)

df['Edad'] = df ['Edad']. round().astype(int)
df['VisitasPorMes'] = df['VisitasPorMes'].round().astype(int)
print (df)
x=df[['Edad','GastoMensual','VisitasPorMes']]

#================================
inertias = []
k_range = range (1,10) 
for k in k_range:
    kmeans = KMeans(n_clusters = k, random_state = 42)
    kmeans.fit(x)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(6,4))
plt.plot(k_range,inertias,marker = 'o')
plt.xlabel('Numero de cluster')
plt.ylabel('Inercia')
plt.title('Método del codo Segmentación de clientes')
plt.show()


df['Edad'] = df ['Edad']. round().astype(int)
df['VisitasPorMes'] = df['VisitasPorMes'].round().astype(int)
print (df)
x=df[['Edad','GastoMensual','VisitasPorMes']]
#======================================
# Entrenar K-Menans con k = 4
#======================================
kmeans = KMeans(n_clusters = 4, random_state = 42)
kmeans.fit(x)
df['Cluster'] = kmeans.labels_

#======================================
# Grafica en 3d con 
#======================================
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111,projection='3d')

# Colocar colores a los cluster
sc = ax.scatter(df['Edad'],df['GastoMensual'],df['VisitasPorMes'],
                c = df['Cluster'],cmap = 'viridis', s = 50)
# Etiqueta de los ejes
ax.set_xlabel('Edad')
ax.set_ylabel('Gastos Mensuales')
ax.set_zlabel('Visitas por mes')
plt.title('Segmentación de clientes Kmeans k = 4')
# Anotacioens interpretativas
ax.text(22,80,2, 'Jovenes bajo gasto \n Pocas visitas',color = 'black')
ax.text(38,480,9, 'Familias alto gasto\n visitas frecuentes',color = 'black')
ax.text(63,310,5, 'Mayores gasto medio\n visitas infrecuentes',color = 'black')
ax.text(33,920,11, 'Clientes VIP\n Gasto muy alto',color = 'black')
plt.show()