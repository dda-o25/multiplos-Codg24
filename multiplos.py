"""
Carlos Osvaldo Díaz García

Fecha
12 de septiembre de 2025

Dados dos números, determinar si uno es múltiplo del otro.
"""

# Entradas
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))

# Proceso

if numero_1>0 and numero_2>0:
    if numero_1 % numero_2 == 0:
        #Salida
        print("El número", numero_1,"es múltiplo del", numero_2)

    if numero_2 % numero_1 == 0:
        #Salida
        print("El número", numero_2,"es múltiplo del", numero_1)
    else:
        #Salida
        print("Ninguno de los números es múltiplo del otro")

if numero_1 == 0:
    #Salida
    print("El número", numero_1,"es múltiplo del", numero_2)

if numero_2 == 0:
    #Salida
    print("El número", numero_2,"es múltiplo del", numero_1)