import java.util.*;
class transposeMatrixSolution
{
    public int[][] transpose(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int[][] res = new int[col][row];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                res[j][i] = matrix[i][j];
            }
        }
        return res;
    }
}
public class transposeMatrix{
    public static void main(String[] args) {
        transposeMatrixSolution s = new transposeMatrixSolution();
        System.out.println("Enter the number of rows and columns of the matrix");
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();
        int[][] matrix = new int[row][col];
        System.out.println("Enter the elements of the matrix");
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                matrix[i][j] = sc.nextInt();
            }
        }
        int[][] res = s.transpose(matrix);
        for(int i=0;i<res.length;i++){
            for(int j=0;j<res[0].length;j++){
                System.out.print(res[i][j]+" ");
            }
            System.out.println();
        }
        sc.close();
    }
}