# PyRoller 2.0
# A program to roll a dice or a coin.
# Author: Nikos-Nikitas
# GitHub: https://github.com/nikosnikitas


import sys
import os
from random import choice, randint


''' Shows the help menu with available options. '''
def help_menu():
    print("PyRoller 2.0 by Nikos-Nikitas")
    print("USAGE : [OPTIONS]")
    print("Available Options")
    print("-h / help : Show this help menu.")
    print("cli : Run in Command Line Interface (CLI) Mode.")
    print("cd / custom : Roll a custom dice. Specify the number of sides.")
    print("c / coin : Throw a coin.")
    print("dN : Roll a dice of N sides.")
    print("Available dices: d4, d6, d8, d10, d12, d20, d30")

''' Gets the sides of the dice to generate. '''
def get_sides():

    try:

        sides_num = int(input("Enter number of sides: "))
        print(f"Custom Dice: {randint(1, sides_num)}")

    except ValueError:
        print("""
        -- VALUE ERROR: Please run again and enter an integer number. --
        """)
        sys.exit()


def main():
    coin = choice(['Heads', 'Tails'])

    d4 = randint(1, 4)
    d6 = randint(1, 6)
    d8 = randint(1, 8)
    d10 = randint(1, 10)
    d12 = randint(1, 12)
    d20 = randint(1, 20)
    d30 = randint(1, 30)

    a = input("Dice or Coin? (D/C) ")

    if a.lower() == "c":
        print(coin)

    elif a.lower() == "d":

        a2 = input("Would you like a custom dice? (Y/N) ")

        if a2.lower() == "n":
            print("Dices rolled\n------------")
            print(f"d4: {d4}")
            print(f"d6: {d6}")
            print(f"d8: {d8}")
            print(f"d10: {d10}")
            print(f"d12: {d12}")
            print(f"d20: {d20}")
            print(f"d30: {d30}")

        elif a2.lower() == "y":
            get_sides()

        else:
            os.system('clear')
            main()

    else:
        os.system('clear')
        main()

''' Checks command line arguments given. '''
def check_args():
    if len(sys.argv) > 2:
        print("-- OPTIONS ERROR: Too many options added. --")
        sys.exit()

    elif len(sys.argv) < 2:
        print("-- OPTIONS ERROR: Not enough options added. --")
        sys.exit()

    else:
        if sys.argv[1] == "-h" or sys.argv[1] == "help":
            help_menu()

        elif sys.argv[1] == "c" or sys.argv[1] == "coin":
            print(f"Coin: {choice(['Heads', 'Tails'])}")

        elif sys.argv[1] == "d4":
            print(f"D4: {randint(1, 4)}")

        elif sys.argv[1] == "d6":
            print(f"D6: {randint(1, 6)}")

        elif sys.argv[1] == "d8":
            print(f"D8: {randint(1, 8)}")

        elif sys.argv[1] == "d10":
            print(f"D10: {randint(1, 10)}")

        elif sys.argv[1] == "d12":
            print(f"D12: {randint(1, 12)}")

        elif sys.argv[1] == "d20":
            print(f"D20: {randint(1, 20)}")

        elif sys.argv[1] == "d30":
            print(f"D30: {randint(1, 30)}")

        elif sys.argv[1] == "cd" or sys.argv[1] == "custom":
            get_sides()

        elif sys.argv[1] == "cli":
            main()


if __name__ == '__main__':
    check_args()
