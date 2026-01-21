import java.util.*;
class setMatrixZeroSolution
{
    public void setZeroes(int[][] matrix)
    {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean rowHasZero = false;
        boolean colHasZero = false;
        for(int i = 0; i < m; i++)
        {
            if(matrix[i][0] == 0)
            {
                colHasZero = true;
                break;
            }
        }
        for(int i = 0; i < n; i++)
        {
            if(matrix[0][i] == 0)
            {
                rowHasZero = true;
                break;
            }
        }
        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                if(matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        if(rowHasZero)
        {
            for(int i = 0; i < n; i++)
            {
                matrix[0][i] = 0;
            }
        }
        if(colHasZero)
        {
            for(int i = 0; i < m; i++)
            {
                matrix[i][0] = 0;
            }
        }
    }
}
public class setMatrixZero
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int m = sc.nextInt();
        System.out.println("Enter the number of columns: ");
        int n = sc.nextInt();
        int[][] matrix = new int[m][n];
        System.out.println("Enter the elements of the matrix: ");
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                matrix[i][j] = sc.nextInt();
            }
        }
        setMatrixZeroSolution obj = new setMatrixZeroSolution();
        obj.setZeroes(matrix);
        System.out.println("The matrix after setting zeroes is: ");
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        sc.close();
    }
}