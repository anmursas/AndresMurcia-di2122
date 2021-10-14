import random
intentos = 0
num = random.randint(0,100)
while intentos < 100:
    print("Adivina: ")
    estimacion = input()
    estimacion = int(estimacion)

    intentos = intentos + 1
    if estimacion < num:
        print("Por bajo")

    if estimacion > num:
        print("Por arriba")

    if estimacion == num:
        break

if estimacion == num:
    intentos = str(intentos)
    print("Buen trabajo has adivinado mi numero ", num ," en intentos: ", intentos)

