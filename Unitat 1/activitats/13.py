import random

acertado = False
num = random.randint(0, 100)
while not acertado:
    try:
        print("Adivina: ")
        estimacion = input()
        estimacion = int(estimacion)
    except ValueError:
        print("Error, valor no númerico")
        break

    if estimacion < num:
        print("Muy bajo")

    if estimacion > num:
        print("Demasiado alto")

    if estimacion == num:
        acertado = True
        break

if estimacion == num:
    print("Enhorabuena, has adivinado el número ", num)
