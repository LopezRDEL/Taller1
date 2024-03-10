#Años bisiestos
import java.util.Scanner;

public class Annos_Bisiestos {

    public static void main(String[] args) {

        Scanner sc = new Scanner (System.in);
        int anno, op, po, pp;

        System.out.println("Ingrese el año:");
        anno = sc.nextInt();

        op = anno % 400;
        po = anno % 4;
        pp = anno % 100;

        if(pp == 0){
            if(op == 0){
                System.out.println("El año "+anno+" es bisiesto.");
            }else{
                System.out.println("El año "+anno+" no es bisiesto.");
            }
        }else{
            if(po == 0){
                System.out.println("El año "+anno+" es bisiesto.");
            }else{
                System.out.println("El año "+anno+" no es bisiesto.");
            }
        }
    }
}
