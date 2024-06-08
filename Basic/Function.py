balance = 0

def showBalance():
    print(f"Your balance is {balance:.2f}")

#function for deposit
def deposit():
    try:
        global balance
        amount = float(input("How much amount: "))
    
        if amount <= 0:
            print("That is not a valid amount")
            return
    
        balance += amount
        print(f"Deposit successful. Your new balance is {balance:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


# Function for withdraw
def withdraw():
    """Function to withdraw money from the balance."""
    try:
        global balance
        amount = float(input("Enter the amount: "))
        
        if amount <= 0:
            print("That is not a valid amount")
            return
    
        if balance < amount:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your new balance is {balance:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


# Banking
def banking():
    isRunning = True

    while isRunning:
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                showBalance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                isRunning = False
                print("Thank you for using the banking program.")
            case _:
                print("That is not a valid choice")

    
# main function
banking()
