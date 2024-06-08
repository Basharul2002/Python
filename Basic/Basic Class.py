class Banking:
    def __init__(self):
        self.balance = 0

    def show_balance(self):
        """Function to display the current balance."""
        print(f"Your balance is {self.balance:.2f}")

    #Function to deposit money into the balance.
    def deposit(self):
        try:
            amount = float(input("How much amount: "))

            if amount <= 0:
                print("That is not a valid amount")
                return

            self.balance += amount
            print(f"Deposit successful. Your new balance is {self.balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    #Function to withdraw money from the balance.
    def withdraw(self):
        try:
            amount = float(input("Enter the amount: "))

            if amount <= 0:
                print("That is not a valid amount")
                return

            if self.balance < amount:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is {self.balance:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def run(self):
        """Function to run the banking program."""
        is_running = True

        while is_running:
            print("\nBanking Program")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    self.show_balance()
                case "2":
                    self.deposit()
                case "3":
                    self.withdraw()
                case "4":
                    is_running = False
                    print("Thank you for using the banking program.")
                case _:
                    print("That is not a valid choice")

if __name__ == "__main__":
    banking_app = Banking()
    banking_app.run()
