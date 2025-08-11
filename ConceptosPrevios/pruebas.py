import numpy as np
import pandas as pd

# 8. Leer dos números y un operador ( +, -, *, / ), realizar la operación indicada,
# indicar con un mensaje si NO reconoce el operador y cuando sea el caso indicar
# que la división por cero es “ERROR” y no permitir realizar las operaciones;
# recomendación crear una sola función que retorne el resultado de la
# operación indicada.

# 10. Dado un número de tres dígitos determinar si es un número CAPICUA o no; un
# número capicúa es el que al leerlo de derecha a izquierda y de izquierda a
# derecha es el mismo, Ejm: 525 es capicúa, mientras que 526 no es capicúa.
# Validar las excepciones,
# • Qué sea un numero entero
# • Que la longitud del número sea de tres dígitos (con la función len(texto)).
# • # Eliminamos el signo negativo y verificamos si tiene 3 dígitos
# • if len(numero.lstrip("-")) == 3

numero = int(input("\n10: \n Escriba numero de 3 cifras para verificar que sea capicua: "))
if ((numero > 99) & (numero < 1000)): 
    if int(numero/100) == (numero % 10):
        print (f"El número {numero}, es un número capicúa")
    else:
        print (f"El número {numero}, no es un número capicúa")
else:
    print ("El número no tine 3 digitos o no es un número")