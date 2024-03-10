import java.util.Scanner;

public class IMC {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float estatura, peso, imc;
        int edad;

        System.out.println("Ingrese su estatura:");
        estatura = sc.nextFloat();

        System.out.println("Ingrese su peso:");
        peso = sc.nextFloat();

        System.out.println("Ingrese su edad:");
        edad = sc.nextInt();

        imc = peso / (estatura * estatura);

        if (edad >= 45) {
            if (imc < 22.0) {
                System.out.println("Está en un riesgo MEDIO de sufrir enfermedades coronarias.");
            } else {
                System.out.println("Está en un riesgo ALTO de sufrir enfermedades coronarias.");
            }
        } else {
            if (imc < 22.0) {
                System.out.println("Está en un riesgo BAJO de sufrir enfermedades coronarias.");
            } else {
                System.out.println("Está en un riesgo MEDIO de sufrir enfermedades coronarias.");
            }
        }
    }
}