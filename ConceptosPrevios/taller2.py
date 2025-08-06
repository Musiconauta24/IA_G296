import pandas as pd
import math

# Taller 2 Python 

# 1. Calificación Final.
# La calificación final de un curso se calcula así: 30% del primer parcial, 30% del
# segundo parcial y 40% del proyecto final.
# Crea una función que calcule la nota final a partir de las tres calificaciones.

Notas = pd.Series ([0,0,0], index = ["par1", "par2", "proy"])
print ("\n1:\n Ingrese las notas del estudiante")
Notas["par1"] = float(input("\nNota de Parcial 1: "))
Notas["par2"]= float(input("\nNota de Parcial 2: "))
Notas["proy"]= float(input("\nNota de Proyecto Final: "))
definitiva = float((Notas["par1"] * 0.3) + (Notas["par2"] * 0.3) + (Notas["proy"] * 0.4))
Notas.loc["Def"] = definitiva
print(f"\n{Notas}")

# 2. Carrera de Atletismo.
# Un atleta corre a una velocidad constante de 8 km/h.
# Escribe una función que indique la distancia recorrida según el tiempo en
# horas.

Tiempo = float(input("\n2: \n Indique el tiempo que lleva corriendo en horas: "))
Distancia = Tiempo * 8
print(f"\nEl atleta ha recorrido {Distancia} km en {Tiempo} horas.")

# 3. Plan de Celular.
# Un plan de celular cuesta $15.000 mensuales e incluye 100 minutos. Cada
# minuto adicional cuesta $200.
# Escribe una función que calcule el costo total del plan según los minutos usados.

plan = 15000
min_incluidos = 100
min_adicional = 200
min_usados = int(input("\n3: \n Ingrese la cantidad de minutos usados: "))
print ("\n El valor de la factura es de: ")
recargo = (min_usados - min_incluidos) * min_adicional
if ((min_usados - min_incluidos) > 0 ):
    print (f" $ {plan} del plan base + $ {recargo} de minutos adicionales:\n Para un total de: $ {(plan + recargo
    )}")
else:
    print (f" $ {plan} del plan base + $ 0 de minutos adicionales:\n Para un total de: $ {(
        plan 
    )}")

#4. Consumo de gasolina
# Un carro consume 1 galón de gasolina por cada 40 kilómetros recorridos.
# Crea una función que indique cuántos galones necesita el carro para recorrer
# cierta distancia

Distancia = float(input("\n4: \n Indique el distancia que necesita recorrer en km: "))
Galones = math.ceil(Distancia/40)
print(f"\n Necestia al menos {Galones} galones de gasolina, para recorrer {Distancia} kilometros")

#5. Entrada al parque
# La entrada a un parque de diversiones cuesta $30.000 por persona. Si un grupo
# de personas va al parque, el total a pagar depende del número de personas.
# Escribe una función que relacione el número de personas con el costo total.

entrada = 30000
Personas = int(input("\n5: \n Indique el número de personas que entrarán al parque: "))
Precio = Personas * entrada
print(f"\n Debe pagar $ {Precio} por la entrada de {Personas} personas")

#6. Costo de envío
# Una empresa de mensajería cobra una tarifa fija de $5.000 por envío, más
# $2.000 por cada kilogramo que pese el paquete.
# Crea una función que represente el costo total del envío según el peso del paquete.

peso = float(input("\n6: \n Indique el peso en kg del paquete que desea enviar: "))
Precio = 5000 + (math.ceil(peso) * 2000)
print(f"\n Debe pagar $ {Precio} por el envío del paquete de {peso} kg")

#7. Costo salario por horas
# Una empresa paga a sus empleados una tarifa fija de $10.000 por hora, más un
# recargo del 100% por cada hora adicional.
# Crea una función que represente el pago total del empleado según el total de
# horas trabajadas.

horas = int(input("\n7: \n Indique el número de horas trabajadas: "))
Precio = int(horas * 10000)
print(f"\n Debe recibir $ {Precio} por las {horas} horas trabajadas")

#8. Ejercicio independiente.
# Plantear de acuerdo a su experiencia o trabajo un ejercicio de su autoría, que
# contengan funciones y resuélvalo.

# Validación de Contraseña
# Escribe una función que valide si una contraseña cumple con los siguientes requisitos: 
# al menos 8 caracteres, contiene una mayúscula, una minúscula y un número.

pin = input("\n8: \n Ingrese la contraseña que desea validar: ")
mayus = 0
minus = 0
num = 0

if len(pin) >= 8:
    for c in pin:
        if c.isupper():
            mayus = mayus + 1
        if c.islower():
            minus = minus + 1
        if c.isdigit():
            num = num + 1
if (num == 0 or minus == 0 or mayus == 0 or len(pin) < 8):
    print(f"La contraseña {pin} no cumple con los requisitos exigidos")
else:
    print(f"La contraseña {pin} cumple con los requisitos exigidos")


#9. Conversión de Moneda
# Escribe una función que reciba una cantidad en pesos colombianos y la convierta a dólares,
# euros y yenes. Usa tasas de cambio fijas, incluyendo una tarifa del 10%.

monto = float(input("\n9: \n Ingrese la cantidad en peso colombiano que quiere cambiar: "))
yen = (monto * 0.0358098)
euro = (monto * 0.0002124)
dolar = (monto * 0.0002472)

print (f"El cambio de {monto} sería: \n{round(
    (yen) * 0.9,2)} yenes considerando un descuento de {round((yen) * 0.1,2)} \n{round(
    (euro) * 0.9,2)} euros considerando un descuento de {round((euro) * 0.1,2)} \n{round(
    (dolar) * 0.9,2)} dolares considerando un descuento de {round((dolar) * 0.1,2
)}")

#10. Promedio de Temperaturas
# Escribe una función que reciba una lista de temperaturas diarias y devuelva e
# l promedio, la máxima y la mínima.

num = int(input ("\n10: \n Indica la número de temperaturas a analizar: "))
temp = pd.Series()
print (f"Ingrese las {num} temperaturas a evaluar:")
for i in range(num):
    temp.loc[i] = float(input(f"\n Temperatura #{i+1}: "))
temp.loc["Prom"] = (sum(temp) / len (temp))
temp.loc["Max"] = max(temp)
temp.loc["Min"] = min(temp)
print(f"\n{temp}")