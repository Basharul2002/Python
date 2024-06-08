class Account:
    def __init__(self, name, account_type, account_no, balance):
        self.AccountHolder = name
        self.AccountType = account_type
        self.AccountNo = account_no
        self.Balance = balance

    def show_account_details(self):
        print(f"Account Holder: {self.AccountHolder}")
        print(f"Account Type: {self.AccountType}")
        print(f"A/c No: {self.AccountNo}")
        print(f"Balance: {self.Balance}")
        print()

    def account_deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Invalid amount. Deposit amount must be greater than zero.")
           
            else:
                self.Balance += amount
                print(f"Deposit of {amount:.2f} successful. Your new balance: {self.Balance:.2f}")
       
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def account_withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: "))
            
            if amount <= 0:
                print("Invalid amount")
                
            elif self.Balance < amount:
                print("Insufficient balance. Transaction cannot be completed.")
                
            else:
                self.Balance -= amount
                print(f"Withdrawal of {amount:.2f} successful. Your new balance: {self.Balance:.2f}")
        
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def transfer_balance(self, other_account, transfer_amount):
        try:
            if transfer_amount <= 0:
                print("Invalid amount")
                
            elif self.Balance < transfer_amount:
                print("Insufficient balance. Transfer cannot be completed.")
                
            else:
                self.Balance -= transfer_amount
                other_account.Balance += transfer_amount
                print(f"Transfer of {transfer_amount:.2f} successful.")
                print("Account 1 details:") 
                self.show_account_details()
                print("Account 2 details:") 
                other_account.show_account_details()
                
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def banking_operations(account):
    while True:
        print("\nBanking Menu")
        print("1. Show Account Details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Balance")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            
            match choice:
                case 1:
                    account.show_account_details()
                    
                case 2:
                    account.account_deposit()
                    
                case 3:
                    account.account_withdraw()
                    
                case 4:
                    other_account = a2 if account == a1 else a1
                    transfer_amount = float(input(f"Enter amount to transfer to {other_account.AccountHolder}'s account: "))
                    account.transfer_balance(other_account, transfer_amount)
                    
                case 5:
                    print("Exiting banking program. Thank you!")
                    break
                
                case _:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Creating instances of Account class
a1 = Account("Basharul Alam", "Personal", "20020106-xxxxxx-22", 500000)
a2 = Account("Humaiyra Khanam", "Personal", "20060921-xxxxxx-25", 80000)

# Main banking operations loop
print("Welcome to the Banking Program\n")

while True:
    print("\nChoose Your Account:")
    print("1. Account-1")
    print("2. Account-2")
    print("3. Exit")

    try:
        account_choice = int(input("Enter your choice: "))
        
        match account_choice:
            case 1: 
                print("\nWelcome,", a1.AccountHolder)
                banking_operations(a1)
            case 2:
                print("\nWelcome,", a2.AccountHolder)
                banking_operations(a2)
            case 3:
                print("Exiting the program. Thank you for using our banking service.")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 3.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

