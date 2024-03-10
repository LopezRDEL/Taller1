numeros = []

print("Ingrese cualquier cuatro números:")

for i in range(4):
    numeros.append(int(input()))

for i in range(4):
    for j in range(4):
        if numeros[i] > numeros[j]:
            acum = numeros[j]
            numeros[j] = numeros[i]
            numeros[i] = acum

print("Los números en orden de mayor a menor son:")

for i in range(4):
    print(numeros[i])