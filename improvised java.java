import java.util.Scanner;

public class EquityBankApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] functionalities = {"Withdraw", "Deposit", "Check Balance", "Transaction History"};
        String option_1 = "yes";
        String option_2 = "Thank you for using Equity Bank, Welcome always.";
        String[] duration = {"1 Month", "3 Months", "6 Months", "12 Months", "2 Years"};
        String[] function1 = {"Agent", "ATM"};
        String[] function2 = {"Direct Deposit", "Bank Transfer"};
        String stored_pin = "1234";

        System.out.println("Welcome to Equity Bank");
        System.out.print("Dear customer, would you like to continue to the main menu? (yes/no): ");
        String prompt = scanner.nextLine().toLowerCase();

        if (prompt.equals(option_1)) {
            System.out.println("Please choose one of the following options:");
            for (int i = 0; i < functionalities.length; i++) {
                System.out.println((i + 1) + ". " + functionalities[i]);
            }

            System.out.print("Enter the number corresponding to your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline after int input

            switch (choice) {
                case 1: // Withdrawal
                    System.out.println("You chose " + functionalities[0]);
                    System.out.println("Please choose your withdrawal method:");
                    for (int i = 0; i < function1.length; i++) {
                        System.out.println((i + 1) + ". " + function1[i]);
                    }

                    int withdrawal_method = scanner.nextInt();
                    scanner.nextLine(); // Consume newline after int input

                    if (withdrawal_method >= 1 && withdrawal_method <= function1.length) {
                        System.out.print("Enter PIN to withdraw: ");
                        String pin = scanner.nextLine();
                        if (pin.equals(stored_pin)) {
                            System.out.println("Withdrawal process initiated via " + function1[withdrawal_method - 1] + ".");
                        } else {
                            System.out.println("Invalid PIN. Transaction aborted.");
                        }
                    } else {
                        System.out.println("Invalid withdrawal method. Please try again.");
                    }
                    break;

                case 2: // Deposit
                    System.out.println("You chose " + functionalities[1]);
                    System.out.println("Please choose your deposit method:");
                    for (int i = 0; i < function2.length; i++) {
                        System.out.println((i + 1) + ". " + function2[i]);
                    }

                    int deposit_method = scanner.nextInt();
                    scanner.nextLine(); // Consume newline after int input

                    if (deposit_method >= 1 && deposit_method <= function2.length) {
                        System.out.print("Enter the amount to deposit: ");
                        double amount = scanner.nextDouble();
                        scanner.nextLine(); // Consume newline after double input
                        System.out.println("Deposit of " + amount + " initiated via " + function2[deposit_method - 1] + ".");
                    } else {
                        System.out.println("Invalid deposit method. Please try again.");
                    }
                    break;

                case 3: // Check Balance
                    System.out.println("You chose " + functionalities[2]);
                    System.out.print("Enter PIN to check balance: ");
                    String pin = scanner.nextLine();

                    if (pin.equals(stored_pin)) {
                        System.out.println("Checking balance... Your balance is...");
                    } else {
                        System.out.println("Invalid PIN. Try again!");
                    }
                    break;

                case 4: // Transaction History
                    System.out.println("You chose " + functionalities[3]);
                    System.out.println("Please choose your transaction period:");
                    for (int i = 0; i < duration.length; i++) {
                        System.out.println((i + 1) + ". " + duration[i]);
                    }

                    int transact_duration = scanner.nextInt();
                    scanner.nextLine(); // Consume newline after int input

                    if (transact_duration >= 1 && transact_duration <= duration.length) {
                        System.out.println("Transaction history for the last " + duration[transact_duration - 1] + ":");
                    } else {
                        System.out.println("Invalid input. Try again!");
                    }
                    break;

                default:
                    System.out.println("Invalid choice. Try again!");
            }
        } else {
            System.out.println(option_2);
        }

        scanner.close();
    }
}
