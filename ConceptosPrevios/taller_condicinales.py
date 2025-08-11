import numpy as np
import pandas as pd

# Taller de estructuras condicionales y de repetición

# 1. Determinar si un número es positivo o negativo
Num = float(input("\n1: \n Escriba el número que desea verificar: "))
if Num < 0: 
    print (f" El número {Num} es Negativo")
else: 
    print (f" El número {Num} es Negativo")

# 2. Determinar si un número es par o impar
Num = int(input("\n2: \n Escriba el número entero que desea verificar: "))
if Num % 2 == 0:
    print (f" El número {Num} es Par")
else:
    print (f" El número {Num} es Impar")

# 3. Determinar si un número es divisible exactamente por 3 y 5 al mismo tiempo,
#por ejemplo 15 cumple, 10 no cumple porque NO es divisible por 3
Num = int(input("\n3: \n Escriba el número entero que desea verificar: "))
if (Num % 3 == 0) & (Num % 5 == 0):
    print (f" El número {Num} es divisible entre 3 y 5")
else:
    print (f" El número {Num} no es divisible entre 3 y 5")

# 4. Leer un carácter, determinar si es una vocal
letra1 = str(input("\n4: \n Escriba la letra que desea verificar: "))[0]
letra = letra1.lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print (f" El caracter '{letra1}' es una vocal")
else:
    print (f" El caracter '{letra1}' no es una vocal")

# 5. Leer una letra por teclado, determinar si es vocal, consonante o digito numérico,
#ayuda ver tabla del código ASCII en internet.
char = str(input("\n5: \n Escriba el caracter que desea verificar: "))[0]
if char.isalpha():
    print (f" El caracter '{char}' es una letra")
elif char.isnumeric():
    print (f" El caracter '{char}' es un número")
else:
    print (f" El caracter '{char}' es una simbolo")

# 6. Leer 3 números, mostrarlos y deducir si se han introducido en orden creciente;
# por ejemplo:
# 1, 2, 3 # se han ingresado en forma creciente
# 3, 1, 2 # NO se han ingresado en forma crecient

Numeros = np.array([0,0,0])
tamaño = len(Numeros)
print (f"\n6: \n Ingrese los {tamaño} números a evaluar:")
for i in range(tamaño):
    Numeros[i] = int(input(f"\n  Dígito #{i+1}: "))
if (Numeros[0] == np.max(Numeros)) & (Numeros[1] == int(np.median(Numeros))) & (Numeros[2] == np.min(Numeros)):
    print (f"  El orden de: {(Numeros)} es correcto")
else:
    print (f"  El orden de: {(Numeros)} es incorrecto\n")
    print (f"  El orden corrento es: [{np.max(Numeros)} {int(np.median(Numeros))} {np.min(Numeros)}]")

# 7. Leer el número del mes, indicar el nombre del mes. Ejm: el mes 1 es ENERO, 12
# es DICIEMBRE, sin no cumple mostrar un mensaje por ejemplo “EL MES 25 NO EXISTE”

Meses = pd.Series ([1,2,3,4,5,6,7,8,9,10,11,12], index = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
mes = int(input("\n1: \n Escriba el mes que desea verificar: "))
if mes < 1 | mes > 12:
    print (f"El mes {mes}, no corresponde a ningun mes")
else:
    print (f"El mes {mes}, corresponde el mes de {Meses.index[mes-1]}")

# 8. Leer dos números y un operador ( +, -, *, / ), realizar la operación indicada,
# indicar con un mensaje si NO reconoce el operador y cuando sea el caso indicar
# que la división por cero es “ERROR” y no permitir realizar las operaciones;
# recomendación crear una sola función que retorne el resultado de la
# operación indicada.

op1 = float(input("\n8: \n Escriba el primer operador: "))
op2 = float(input("\n Escriba el segundo operador: "))
op = str(input("\n Determina la operación que deseas realizar (+,-,*,/): "))[0]
if op == "+":
     print (f"La operación es suma: \n {op1} + {op2} = {(op1 + op2)}")
elif op == "-":
     print (f"La operación es resta: \n {op1} - {op2} = {(op1 - op2)}")
elif op == "*":
     print (f"La operación es multiplicación: \n {op1} * {op2} = {(op1 * op2)}")
elif op == "/":
     print (f"La operación es División: \n {op1} / {op2} = {(op1 / op2)}")
else:
     print (f"La operación {op} no está definida")

# 9. Realizar un programa que permita realizar la preselección del integrante del
# equipo de baloncesto, cuyo requisito es tener más de 1.80 mts. de estatura y
# pesar menos de 100 Kg. Indicar si es APTO o no lo es.

altura = float(input("\n9: \n Escriba la altura en metros del jugador: "))
peso = float(input("\n Escriba el peso en kilogramos del jugador: "))
if (altura < 1.8) and (peso < 100):
    print ("El jugador no cumple los requisitos para acceder al equipo")
else:
    print ("El jugador cumple los requisitos para acceder al equipo")

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