import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

## 🧩 Actividades
#1. Crear una Serie con los nombres y alturas de los estudiantes

print (f"\n 1: { pd.DataFrame(
    datos_estudiantes,
    columns = ["altura"]
)}")

#Pregunta: ¿Cuál es la altura de Daniela?

print (f"\n 1.1:\n{ pd.DataFrame(
    datos_estudiantes,
    columns = ["altura"],
    index = ["Daniela"]
)}")

#2. Accede al promedio de calificación de Carlos de 3 formas diferentes:

print (f"\n 2:\n a){ pd.DataFrame(
    datos_estudiantes,
    columns = ["promedio"],
    index = ["Carlos"]
)}")

print (f"\n b) { (
    df["promedio"].iloc[1]
)}")

print (f"\n c) { (
    df["promedio"].loc["Carlos"]
)}")
 

#3. Filtra a los estudiantes con promedio mayor o igual a 4.0
 
print (f"\n 3:\n{(
    df["promedio"]>=4.0
)}")
 

#Pregunta: ¿Cuántos estudiantes tienen un buen promedio?

bprom = df.query("promedio >= 4")
bprom = len(bprom)
print (f"\n 3.1:\n{(
    bprom
)}")

#4. Calcula operaciones estadísticas:

 

#5. Agrega una nueva columna que indique si el estudiante es mayor de edad

adultos = (df["edad"]>17)
df2 = df.copy()
df2["adulto"] = adultos
print (f"\n 5:\n{(
    df2
)}")

#6. Agrega una columna con el año de nacimiento (suponiendo que estamos en 2025)
 
df3 = df.copy()
año = 2025 - df3["edad"]
df3["Nacimiento"] = año
print (f"\n 6:\n{(
    df3
)}")

#7. Visualiza los promedios de los estudiantes en un gráfico
 
df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
plt.show()

#8. Filtra a los estudiantes con altura entre 165 y 175 cm
 
print (f"\n 8:\n{(
    df.query("altura >= 165 and altura <= 175")
)}")


#9. Copia el DataFrame y elimina la columna "peso"
 
df4 = df.copy()
del df4["peso"]
print (f"\n 9:\n{(
    df4
)}")

#10. Crea un nuevo DataFrame con solo 3 columnas: nombre, edad y año de nacimiento
nuevos_datos = {
  "Nacimiento": pd.Series(año, index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}
dfn = pd.DataFrame(nuevos_datos)
dfn["edad"] = 2025 - dfn["Nacimiento"]
print (f"\n 10:\n{(
    dfn
)}")
