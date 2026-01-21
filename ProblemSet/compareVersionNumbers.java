import java.util.*;
class compareVersionNumbersSolution
{
    public int compareVersion(String version1,String version2)
    {
         String[] v1 = version1.split("\\.");
            String[] v2 = version2.split("\\.");
            int i = 0;
            while(i<v1.length || i<v2.length)
            {
                if(i<v1.length && i<v2.length)
                {
                    if(Integer.parseInt(v1[i])>Integer.parseInt(v2[i]))
                    {
                        return 1;
                    }
                    else if(Integer.parseInt(v1[i])<Integer.parseInt(v2[i]))
                    {
                        return -1;
                    }
                }
                else if(i<v1.length && i>=v2.length)                
                {
                    if(Integer.parseInt(v1[i])>0)
                    {
                        return 1;
                    }
                }
                else if(i<v2.length && i>=v1.length)
                {
                    if(Integer.parseInt(v2[i])>0)
                    {
                        return -1;
                    }
                }
                i++;
            }
            return 0;
    }
}
class compareVersionNumbers
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter version 1:");
        String version1 = sc.nextLine();
        System.out.println("Enter version 2:");
        String version2 = sc.nextLine();
         compareVersionNumbersSolution solution = new compareVersionNumbersSolution();
        int result = solution.compareVersion(version1,version2);
        System.out.println(result);
        sc.close();

    }
}