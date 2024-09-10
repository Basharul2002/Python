import pyfiglet as f
import colorama
import time
import os
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

# Function to create a heart shape with Prioty's name
def heart_with_name():
    heart_shape = '\n'.join(
        [''.join(
            [(Fore.RED + '❤️' if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
             for x in range(-30, 30)]
        ) for y in range(15, -15, -1)]
    )
    print(heart_shape)
    print(Fore.LIGHTYELLOW_EX + "\n" + " " * 12 + "P  r  i  o  t  y" + " " * 12)

# Function to create animated text
def animated_text(text, color=Fore.CYAN, delay=0.1):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to print the birthday wish
def birthday_wish():
    # Clear the screen
    clear_screen()
    
    # Print a beautiful heart with Prioty's name
    heart_with_name()
    
    # Print decorative lines
    decorative_line = Fore.MAGENTA + "*" * 50
    print("\n" + decorative_line)
    
    # Print the stylish birthday wish in three lines
    birthday_text = (
        "Happy \n" 
        "Birthday\n"
        "Prioty!\n"
    )
    wish_art = f.figlet_format(birthday_text, font="starwars")
    print(Fore.CYAN + wish_art)
    
    # Print a personalized message with animation
    animated_text("In every algorithm, in every line of code,", Fore.YELLOW, delay=0.05)
    animated_text("You're the constant that makes my heart explode.", Fore.YELLOW, delay=0.05)
    animated_text("Like stars in the debug window, you light up my mind,", Fore.YELLOW, delay=0.05)
    animated_text("My dearest Prioty, you're the best find.", Fore.YELLOW, delay=0.05)
    print()
    animated_text("On this special day, I compile my love for you,", Fore.RED, delay=0.05)
    animated_text("Wrapped in the syntax of a heart so true.", Fore.RED, delay=0.05)
    animated_text("May our connection grow stronger with each passing byte,", Fore.RED, delay=0.05)
    animated_text("Forever and always, in every coding night.", Fore.RED, delay=0.05)
    
    # Print decorative lines with emojis
    emojis = "🎉 🎂 🎈 🎁 ✨"
    print("\n" + decorative_line)
    animated_text(emojis + "  Happy Birthday to the Most Special Person!  " + emojis, Fore.GREEN, delay=0.05)
    print(decorative_line)

# Run the birthday wish function
birthday_wish()
