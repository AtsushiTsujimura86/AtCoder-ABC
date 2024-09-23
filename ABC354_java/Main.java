import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    int H = scanner.nextInt();
    double s = 0;
    int d = 0;
    do {
    	s += Math.pow(2, d);
    	d++;
    }while(H >= s);
    System.out.println(d);
  }
}