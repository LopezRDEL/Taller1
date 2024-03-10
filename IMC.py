estatura = float(input("Ingrese su estatura: "))
peso = float(input("Ingrese su peso:"))
edad = int(input("Ingrese su edad: "))

imc = peso / estatura

if edad >= 45 :
    if imc < 22.0 :
        print("Esta en un riesgo MEDIO de sufrir enfermedades coronarias.")
    else :
        print("Esta en un riesgo ALTO de sufrir enfermedades coronarias.")
else :
    if imc < 22.0 :
        print("Esta en un riesgo BAJO de sufrir enfermedades coronarias.")
    else :
        print("Esta en un riesgo MEDIO de sufrir enfermedades coronarias.")