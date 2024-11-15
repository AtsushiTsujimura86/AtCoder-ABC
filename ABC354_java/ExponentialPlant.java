import java.util.*;

public class ExponentialPlant{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        // int H = Integer.parseInt(scanner.nextLine());
        int pH = 0;
        int cnt = 0;
        while(H >= pH){
            pH += Math.pow(2, cnt++);
            System.out.println("pH: "+ pH);
            System.out.println("cnt: "+ cnt);
            
        }
        System.out.println(cnt);
        scanner.close();
    }
}