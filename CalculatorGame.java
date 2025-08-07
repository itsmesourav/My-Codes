import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CalculatorGame {
    private List<Integer> numbers = new ArrayList<>();
    private int target = 0;
    private boolean gameOver = false;
    private Scanner scanner = new Scanner(System.in);

    public void addNumber() {
        if (!gameOver) {
            System.out.print("Enter a number: ");
            String input = scanner.nextLine();

            if (input.matches("\\d+")) {
                int num = Integer.parseInt(input);
                if (!numbers.contains(num)) {
                    numbers.add(num);
                    System.out.println("Numbers added: " + numbers);
                    addNumber();
                } else {
                    // Remove the duplicate number
                    numbers.remove(Integer.valueOf(num));
                    System.out.println("Duplicated number removed.");
                }
            } else {
                System.out.println("Invalid input. Please enter a digit.");
            }
        } else {
            System.out.println("Game Over!");
            System.exit(0);
        }
    }

    public void resetGame() {
        numbers.clear();
        target = 0;
        System.out.println("New game starting...");
    }

    public void showResult() {
        if (gameOver) {
            System.out.println("Game Over! Final score: " + (target * 10));
            System.exit(0);
        } else {
            int total = numbers.stream().mapToInt(Integer::intValue).sum();
            System.out.println("Your final score is " + total);
        }
    }

    public void play() {
        if (!gameOver) {
            String instruction = "Please enter one or more digits between 1 and 10. Try to reach the target "
                    + "number.\n\nStart the game by clicking 'Add Number' or press any key!\n\nFinal score: " + (target * 10);
            System.out.println(instruction);
            this.addNumber();
        }
    }

    public static void main(String[] args) {
        CalculatorGame game = new CalculatorGame();
        game.play();
    }
}
