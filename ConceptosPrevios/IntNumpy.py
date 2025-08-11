import numpy as np
import matplotlib.pyplot as plt 

# Crea un arreglo de ceros de 3 filas y 4 columnas
a = np.zeros((3, 4))  
print(a)

# Crea un arreglo de unos de 2 filas y 5 columnas
b = np.ones((2, 5))  
print(b)

# Imprime las dimensiones del arreglo a
print ("Dimensiones de a:", a.shape)  

# Imprime el número de dimensiones del arreglo b
print ("Numero de dimensiones de b:", b.ndim)  

#Imprimir el tamaño de la matriz a
print ("Tamaño de a:", a.size)

# Array o Matriz cuyos valores son todo el valor
# indicado como segundo parámetro de la función

c = np.full((2,3,4), 8)
print(c)

# Inicializa los valores del array con lo que haya en memoria en el momento
# El llenado del empty es aleatorio, no se puede predecir
d = np.empty((2,3,9))
print(d)

print("tamaño de d:", d.shape)

#Crear array basada en rangos de valores (minimo, máximo, numero de elementos)

e = np.linspace(0, 6, 10)  # 10 valores entre 0 y 6
print(e)

# Inicar un array con valores aleatorios entre 0 y 1
f = np.random.rand(2,3,4)  # Array de 2x3 con valores aleatorios 
print(f)

# Inicialización de valores aleatorios conformes a una distribución normal
g = np.random.randn(2,3) 
print(g)

# Inicializar un array con valores aleatorios enteros
h = np.random.randint(0, 10, (2,3))  # Valores entre 0 y 10 en un array de 2x3
print(h)

# histograma de valores aleatorios
i = np.random.rand(100) 
plt.hist(i, bins=50, density=True)
plt.show()

# Histograma con valores personalizados
j = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
plt.hist(j, bins=10)
plt.show()

# Inicialización de un array/matriz usando una función
def func(x, y):
    return x + 2*y
k = np.fromfunction(func, (3, 5),)
print(k)

#Acceso a los elementos de un array/matriz unidimensional
array_uni = np.array([1, 2, 3, 4, 5,7,8,9])
print("Shape de array_uni:", array_uni.shape)
print("Primer elemento:", array_uni)
#Acceso al segundo elemento
print("Segundo elemento:", array_uni[1])
#Acceso a los elementos desde la posición 2 al 5
print("Elementos de la posición 2 a la 5:", array_uni[2:5])
#Acceso a los elementos desde la posición 1 haciendo saltos de 3 
print("Elementos de la posición 1 a la 3:", array_uni[1::3])

# Array/matriz multidimensional
array_multi = np.array([[1, 2, 3,4 ], [5,6,7,8]])
print("Shape de array_multi:", array_multi.shape)
print("Primer elemento:", array_multi)

#Acceso al cuarto elemento del array multi
print("Cuarto elemento:", array_multi[0, 3])  

#Acceso a la segunda fila del array multi
print("Segunda fila:", array_multi[1, :])

#Acceder al tercer elemento de las dos filas
print("Tercer elemento de las dos filas:", array_multi[:2,2])

#Modificación de un elemento del array multi con elementos del 0 al 27
array_multi1 = np.arange(24)
print("Array multi modificado:\n", array_multi1.shape)
print(array_multi1)

#Cambiar las dimensiones del array multi a 3 filas y 9 columnas
array_multi1.shape = (6,4)
print("Array multi con nuevas dimensiones:\n", array_multi1)