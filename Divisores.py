dividiendo = int(input("Ingresa los valores en orden: Dividiendo - Divisor: "))
divisor = int(input())

if divisor == 0:
    print("¡No se pueden hacer divisiones entre cero!")
else:
    cociente = dividiendo // divisor
    residuo = dividiendo % divisor
    if residuo == 0:
        print("División exacta.\nCociente:", cociente)
    else:
        print("División inexacta.\nCociente: " + str(cociente) + "\nResiduo: " + str(residuo))