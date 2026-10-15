import random

numeroA = random.randint(1, 20)
intentos = 1
while True:
    numeroB = int(input("introduce un numero(1-20): "))
    if numeroB == numeroA:
        print(f"acertaste en {intentos} intentos!!!")
        break
    else:
        if numeroB > numeroA:
            print("Es menor")
            intentos = intentos + 1
        else:
            print("Es mayor")
            intentos = intentos + 1
