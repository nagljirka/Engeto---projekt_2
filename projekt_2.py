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
number_random = str(random.randint(1000, 9999))


def guess_number(number):
    global bulls
    global cows
    number_used = []
    for i in range(4):
        if number_random[i] == number[i]:
            number_used.append(number[i])
            bulls += 1
            if number[i] in number_random and number_random[i] != number[i] and number[i] not in number_used:
                cows += 1

# Vypsání počtu bulls/cows            
def you_win(bull_count, cows_count):
    bulls_text = f"Bull: {bull_count}" if bull_count <= 1 else f"Bulls: {bull_count}"
    cows_text = f"Cow: {cows_count}" if cows_count <= 1 else f"Cows: {cows_count}"
    print(f"{bulls_text} {cows_text}")

# Hodnocení výsledku
def score():
    if lives <= 2:
        print("That's amazing!")
    elif lives <= 3:
        print("That's average!")
    else:
        print("That's not so good!")

# Počet životů
lives = 0
def zivoty():
    global lives
    if number_input != number_random:
        lives += 1
    else:
        lives += 1
        print("Correct, you've guessed the right number")
        print("in", lives, "guesses!")

# Ošetření vstupů + průběh
while True:
    bulls = 0
    cows = 0
    number_input = input("Enter a number:\n")
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
    zivoty()
    if number_input == number_random:
        score()
        break

    
    
    

    
