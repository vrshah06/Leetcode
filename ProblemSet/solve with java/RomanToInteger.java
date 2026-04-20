import java.util.Scanner;

class RomanToIntegerSolution {
    // Method to convert Roman numeral to integer
    public int romanToInt(String s) {
        int n = s.length();
        int ans = 0;

        // Traverse through the Roman numeral string
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'I') {
                if (i + 1 < n && s.charAt(i + 1) == 'V') {
                    ans += 4;
                    i++;
                } else if (i + 1 < n && s.charAt(i + 1) == 'X') {
                    ans += 9;
                    i++;
                } else {
                    ans += 1;
                }
            } else if (s.charAt(i) == 'V') {
                ans += 5;
            } else if (s.charAt(i) == 'X') {
                if (i + 1 < n && s.charAt(i + 1) == 'L') {
                    ans += 40;
                    i++;
                } else if (i + 1 < n && s.charAt(i + 1) == 'C') {
                    ans += 90;
                    i++;
                } else {
                    ans += 10;
                }
            } else if (s.charAt(i) == 'L') {
                ans += 50;
            } else if (s.charAt(i) == 'C') {
                if (i + 1 < n && s.charAt(i + 1) == 'D') {
                    ans += 400;
                    i++;
                } else if (i + 1 < n && s.charAt(i + 1) == 'M') {
                    ans += 900;
                    i++;
                } else {
                    ans += 100;
                }
            } else if (s.charAt(i) == 'D') {
                ans += 500;
            } else if (s.charAt(i) == 'M') {
                ans += 1000;
            }
        }

        return ans;
    }
}

public class RomanToInteger {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read the Roman numeral input
        String s = sc.next();

        // Create an instance of the Solution class
        RomanToIntegerSolution solution = new RomanToIntegerSolution();

        // Call the romanToInt method and print the result
        int result = solution.romanToInt(s);
        System.out.println(result);

        sc.close();
    }
}
