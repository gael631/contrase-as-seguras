import random
import string

# Etapa 1: variable con todos los caracteres posibles
character = ("+-/*!&$#?=@"
             "abcdefghijklnopqrstuvwxyz"
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "1234567890")

# Etapa 2: pedir longitud (con validación)
def pedir_longitud():
    while True:
        entrada = input("¿Qué tan larga será su contraseña? (número entero): ").strip()
        try:
            largo = int(entrada)
            if largo <= 0:
                print("La longitud debe ser mayor que 0.")
                continue
            return largo
        except ValueError:
            print("Escribe un número entero válido.")

# Programa principal
while True:
    respuesta = input("¿Quieres una nueva contraseña? (si/no): ").strip().lower()
    if respuesta != "si":
        print("Hasta luego.")
        break

    largo = pedir_longitud()          # Etapa 2

    password = ""                      # Etapa 3: variable donde se almacena
    for _ in range(largo):             # Etapa 4: bucle + random.choice
        password += random.choice(character)

    print("Su contraseña es:", password)   # Etapa 5: imprimir

    cambiar = input("¿Quieres cambiarla por una propia? (si/no): ").strip().lower()
    if cambiar == "si":
        password = input("Ingresa la nueva contraseña: ")
        print("Ok, entonces su contraseña es:", password)
    else:
        print("Ok, su contraseña se mantiene:", password)