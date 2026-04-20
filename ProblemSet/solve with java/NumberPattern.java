import java.util.Scanner;

public class NumberPattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Take input from the user for number of rows
        System.out.print("Enter the number of rows: ");
        int n = scanner.nextInt();

        // Outer loop for each row
        for (int i = 1; i <= n; i++) {
            // Inner loop to print numbers in each row
            for (int j = 1; j <= i; j++) {
                System.out.print((i+j)%2 +" ");
            }
            System.out.println(); // Move to the next line after each row
        }

        scanner.close();
    }
}
