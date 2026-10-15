suma = 0
limite = int(input("introduce el limite: "))
pares = 1
for pares in range(1, limite+1):
    if pares%2 == 0:
        suma = suma + pares
    else:
        continue
print(f"La suma de los pares es: {suma}")
