import java.util.Scanner;
class rectangleAreaSolution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) 
    {
        int area1 = (ax2-ax1)*(ay2-ay1);
        int area2 = (bx2-bx1)*(by2-by1);
        int overlap = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1)) * Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1));
        return area1 + area2 - overlap;
    }
}
public class rectangleArea
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int ax1 = sc.nextInt();
        int ay1 = sc.nextInt();
        int ax2 = sc.nextInt();
        int ay2 = sc.nextInt();
        int bx1 = sc.nextInt();
        int by1 = sc.nextInt();
        int bx2 = sc.nextInt();
        int by2 = sc.nextInt();
        rectangleAreaSolution solution = new rectangleAreaSolution();
        int result = solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2);
        System.out.println(result);
        sc.close();
    }
}