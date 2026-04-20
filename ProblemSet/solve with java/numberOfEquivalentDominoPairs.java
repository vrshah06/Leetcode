import java.util.*;
class numberOfEquivalentDominoPairsSolution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int count = 0;
        for(int i = 0;i<dominoes.length;i++)
        {
            for(int j = i+1;j<dominoes.length;j++)
            {
                if((dominoes[i][0] == dominoes[j][0] && dominoes[i][1] == dominoes[j][1]) || (dominoes[i][0] == dominoes[j][1] && dominoes[i][1] == dominoes[j][0]))
                {
                    count++;
                }
            }
        }
        return count;
    }
}
public class numberOfEquivalentDominoPairs {
    public static void main(String[] args) {
        numberOfEquivalentDominoPairsSolution solution = new numberOfEquivalentDominoPairsSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of dominoes: ");
        int n = scanner.nextInt();
        int[][] dominoes = new int[n][2];
        System.out.println("Enter the dominoes (two numbers for each domino): ");
        for (int i = 0; i < n; i++) {
            dominoes[i][0] = scanner.nextInt();
            dominoes[i][1] = scanner.nextInt();
        }
        scanner.close();
        int result = solution.numEquivDominoPairs(dominoes);
        System.out.println("Number of equivalent domino pairs: ");
        System.out.println(result); 
    }
}

