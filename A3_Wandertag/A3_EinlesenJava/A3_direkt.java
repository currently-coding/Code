import java.util.Scanner;
/** 
 * @author: Benjamin Sauerstein
 * Date:    13.09.2024
 * Fuer die 3. Aufgabe des 43. Bundeswettbewerbs Informatik
 */

public class A3_direkt{    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        in.nextLine();
        int wege[][] = new int[s][2];
        for (int i=0; i<s; i++){  
            String zeile = in.nextLine();
            String l[] = zeile.split(" ");
            wege[i][0] = Integer.parseInt(l[0]);
            wege[i][1] = Integer.parseInt(l[1]);
        }
        System.out.println("Die erste Person geht minimal " + wege[0][0] + " Kilometer und maximal " + wege[0][1] + " Kilometer");
    }
}
