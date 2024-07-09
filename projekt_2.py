"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jiří Nágl
email: nagl.jirka@seznam.cz
discord: jirkanagl
"""

import random
print("Hi, there")
print(50 * "-")
print("I've generated a random 4 digit number for you", "Let's play a bulls and cows game.", sep="\n")
print(50 * "-")
# generování náhodneho čísla

def generate_number_random():
    """ Fuknce vygeneruje náhodné čtyřmístné číslo bez duplicit. """
    global number_random
    while True:
        number_random = str(random.randint(1000, 9999))
        print(number_random)
        number_list = list(number_random)
        if len(number_list) != len(set(number_list)):
            pass
        else:
            break
    return number_random


def guess_number(number):
    """ Funkce počítá bulls/cows z vloženého čísla. """
    global bulls
    global cows
    for i in range(4):
        if number_random[i] == number[i]:
            bulls += 1
        if number[i] in number_random and number_random[i] != number[i]:
            cows += 1

# Vypsání počtu bulls/cows            
def you_win(bull_count, cows_count):
    """ Vypsání "s" na konci slova podle množného čísla. """
    bulls_text = f"Bull: {bull_count}" if bull_count <= 1 else f"Bulls: {bull_count}"
    cows_text = f"Cow: {cows_count}" if cows_count <= 1 else f"Cows: {cows_count}"
    print(f"{bulls_text} {cows_text}")

# Hodnocení výsledku
def score():
    """ Funkce vyhodnotí výsledek uživatele. """
    if lives_counter <= 2:
        print("That's amazing!")
    elif lives_counter <= 3:
        print("That's average!")
    else:
        print("That's not so good!")

# Ošetření vstupů + průběh
generate_number_random()
lives_counter = 0
while True:
    bulls = 0
    cows = 0
    lives_counter += 1
    number_input = input("Enter a number:\n")
    number_input_list = list(number_input)
    if len(number_input_list) != len(set(number_input_list)):
        print("Contains duplicates")
        continue
    if len(number_input) != 4:
        print("Enter 4 numbers!")
        continue 
    if number_input[0] == "0":
        print("Number must not start with 0!")
        continue
    if not number_input.isnumeric():
        print("Není číslo!")
        continue
    if number_input != number_random:
        guess_number(number_input)
        you_win(bulls, cows)
    if number_input == number_random:
        break
print("Correct, you've guessed the right number")
print("in", lives_counter, "guesses!")
score()

    
    
    

    
