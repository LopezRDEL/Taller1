a = float(input("Ingrese los tres lados del triángulo:\n"))
b = float(input())
c = float(input())

suma = a + b
suma2 = b + c
suma3 = a + c

if c > suma or a > suma2 or b > suma3:
    print("El triángulo es inválido")
else:
    if a == b:
        if a == c:
            print("Es un triángulo equilátero.")
        else:
            print("Es un triángulo isósceles.")
    else:
        if a == c:
            print("Es un triángulo isósceles.")
        else:
            if b == c:
                print("Es un triángulo isósceles.")
            else:
                print("Es un triángulo escaleno.")