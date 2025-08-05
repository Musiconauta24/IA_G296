# Introducción Pandas
Python 3.13.2

## Librerías
import pandas as pd
import numpy as np
import matplotlib as plt

# Creación de Objeto Serie

s = pd.Series([2,4,6,8,10])
print(s)

#Creación de un objeto Serie inicializando con un directorio de python 
altura = {"Santiago":180, "Marcelo":172, "Luis":174, "Alejandra":160}
s = pd.Series(altura)
print (s)

"""
Creación de un objeto series inicializandolo con algunos 
de los elementos de un diaccionario de python
"""
altura = {"Santiago":180, "Marcelo":172, "Luis":174, "Alejandra":160}
s = pd.Series(altura, index = ["Marcelo", "Luis"])
print (s)

#Cración de un objeto Series inicializandolo con un escalar
s = pd.Series (34,["test1", "test2", "test3"])
print (s)

"""
Acceso a los elementos de un objeto Series
Cada delemento de objeto series tiene un identificador único"""
s = pd.Series ([2,4,6,8], index = ["num1", "num2", "num3", "num4"])
print (s)

#Accediento al tercer elemento del objeto por el index
print (s["num3"])

#Acceder al elementdo del objeto por la posición
print (s.iloc[2])
print (s.loc["num3"])

#Acceder al segundo y tercer elemento por posición
#en el formato de [posición inicial : posición final menos uno]
print (s.iloc[1:3])

## Operación Aritmética con series 
#Sumar
print (f"suma = {np.sum(s)}")
print ("suma =", np.sum(s))

#Creación de un objeto series denominado temperarutas (temp)
temp = pd.Series ([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s = pd.Series (temp,name = "Temperaturas")
print (s)
s.plot()
plt.show()


# Creación de Objetos DataFrame
#Creación de Objetos DataFrame correspondiente a un diccionario con 3 terminos
personas = {
    "peso": pd.Series ([90,80,70,60],["Santiago", "Marcelo", "Luis", "Alejandra"]),
    "altura": pd.Series ({"Santiago":180, "Marcelo":172, "Luis":174, "Alejandra":160}),
    "hijos": pd.Series ([2,3],["Luis","Marcelo"])
    }
df = pd.DataFrame(personas)
print (df)

#Imprimir en forma de tupla inmutable
df2 = pd.DataFrame(
    personas, 
    columns = ["altura", "peso"],
    index = ["Santiago", "Marcelo", "Luis"]
)
print (df2)

#Acceso a los elementos del df
print (df["peso"])

#Filtrar elementos a mostrar, según condicion boolenana
print ((df["peso"]>60) & (df["peso"]<=80))

#Acceder a los elementos del diccionario según su posición [1:3], correspondientes a las filas 2 y 3
print (df.iloc[1:3])

#Consultas avanzadas
print (df.query("altura >= 170 and peso > 70"))

#Copiar un DataFrame
df_copy = df.copy()

#Añadir una nueva columna al DataFrame
df_copy["Cumpleaños"] = [1990, 1978, 1980,1994]
print (df_copy)

#Añadir una nueva columna calculada
df_copy["años"] = 2025 - df_copy["Cumpleaños"]
print (df_copy)