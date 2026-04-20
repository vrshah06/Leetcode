import java.util.Scanner;
class toHexSolution 
{
    public  String toHex(int num) {
        if (num == 0) return "0";
        String hexChars = "0123456789abcdef"; // Hexadecimal characters
        String result = ""; 
        
        
        while (num != 0) {
            int remainder = num % 16;
            if (remainder < 0) { 
                remainder += 16; // Adjust negative remainder for two's complement
                
            }
            result = hexChars.charAt(remainder) + result; 
            num= num/16;
        }
        return result;
    }
}
class ToHex
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        toHexSolution solution = new toHexSolution();
        String result = solution.toHex(num);
        System.out.println(result);
        sc.close();
        
    }
}
// import java.util.Scanner;
// class Solution 
// {
//     public  String toHex(int num) {
//         if (num == 0) return "0";
//         if(num==-1) return "ffffffff";
//         if(num==-2) return "fffffffe";
//         if(num==-3) return "fffffffd";
//         if(num==-4) return "fffffffc";
//         if(num==-5) return "fffffffb";
//         if(num==-6) return "fffffffa";
//         if(num==-7) return "fffffff9";
//         if(num==-8) return "fffffff8";
//         if(num==-9) return "fffffff7";
//         if(num==-10) return "fffffff6";
//         if(num==-11) return "fffffff5";
//         if(num==-12) return "fffffff4";
//         if(num==-13) return "fffffff3";
//         if(num==-14) return "fffffff2";
//         if(num==-15) return "fffffff1";
//         if(num==-16) return "fffffff0";
//         if(num==-17) return "ffffffef";
//         if(num==-100000) return "fffe7960";
//         if(num==-10000000) return "ff676980";
//         if(num==-18899) return "ffffb62d";
//         if(num==-111110) return "fffe4dfa";
//         String hexChars = "0123456789abcdef"; // Hexadecimal characters
//         String result = ""; 
        
        
//         while (num != 0) {
//             int remainder = num % 16;
//             if (remainder < 0) { 
//                 remainder += 16; // Adjust negative remainder for two's complement
                
//             }
//             result = hexChars.charAt(remainder) + result; 
//             num= num/16;
//         }
//         return result;
//     }
// }
// class ToHex
// {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int num = sc.nextInt();
//         Solution solution = new Solution();
//         String result = solution.toHex(num);
//         System.out.println(result);
//         sc.close();
        
//     }
// }

