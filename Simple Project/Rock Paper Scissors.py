import random

options = ["rock", "paper", "scissors"]

userWin = computerWin = 0

random_number = random.randint(0, 2)

while True:
    userInput = input("Enter Rock/Paper/Scissors and Q to Quit: ").lower()

    if userInput == "q":
        break
    
    if userInput not in options:
        print("Invalid Input")
        continue

    computerInput = options[random.randint(0, 2)]

    print(f"Computer picked: {computerInput}")
    if (
            (userInput == 'rock' and computerInput == 'scissors') or 
            (userInput == 'paper' and computerInput == 'rock') or 
            (userInput == 'scissors' and computerInput == 'paper') 
        ):
        print("You won!")
        userWin =+ 1 

    
    else :
        print("Computer won!")
        computerWin += 1

print(f"You won {userWin} times")
print(f"Computer won {computerWin} times")



