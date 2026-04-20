import java.util.*;
class rockPaperScissors
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENter your name: ");
        String name = sc.nextLine();
        System.out.println("Enter your age: ");
        int age = sc.nextInt();
        if(age<0)
        {
            System.out.println("INvalid age.Game ended.");
            System.exit(0);
        }
        System.out.println("Game rules: ");
        System.out.println("1. Rock beats Scissors");
        System.out.println("2. Scissors beats Paper");
        System.out.println("3. Paper beats Rock");
        System.out.println("Let's start the game");
        System.out.println(" ");
        System.out.println("Press 1 for Rock, 2 for Paper, 3 for Scissors");
        System.out.println("");
        int userScore = 0;
        int compScore = 0;
        for(int i=0;i<5;i++)
        {
            
            System.out.println("Round: "+(i+1));
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            if(choice<1 || choice>3)
            {
                System.out.println("Invalid choice");
                System.exit(0);
            }
           int compChoice = (int)(Math.random()*3)+1;
            System.out.println("Computer's choice: "+compChoice);
            if(choice==compChoice)
            {
                System.out.println("It's a tie");
            }    
            else if(choice==1 && compChoice==3 || choice==2 && compChoice==1 || choice==3 && compChoice==2)
            {
                System.out.println(name+" wins");
                userScore++;
            }
            else
            {
                System.out.println("Computer wins");
                compScore++;
            }
            System.out.println("Score: " + name + ": " + userScore);
            System.out.println("");
            System.out.println("Score: Computer: " + compScore);
            System.out.println("");
            if(userScore>compScore)
            {
                System.out.println(name+" wins the game");
            }
            else if(userScore<compScore)
            {
                System.out.println("Computer wins the game");
            }
            else
            {
                System.out.println("It's a tie");
            }
        }
        sc.close();
    }
}
