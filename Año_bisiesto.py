anno = int(input("Ingrese el año:"))

op = anno % 400
po = anno % 4
pp = anno % 100

if pp == 0:
    if op == 0:
        print("El año", anno, "es bisiesto.")
    else:
        print("El año", anno, "no es bisiesto.")
else:
    if po == 0:
        print("El año", anno, "es bisiesto.")
    else:
        print("El año", anno, "no es bisiesto.")