from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

def scrape(URL, rankings):
    soup = BeautifulSoup(urlopen(URL), "html.parser")
    span_elements = soup.find_all('span', class_='s2')
    country_rank = 1

    # Only items 8 through 215 are countries
    for span in span_elements[7:214]:
        country_name = span.text.strip('"')
        rankings[country_name] = country_rank
        country_rank += 1
    print(len(rankings))

def win(choices):
    for i in range(9):
        # Split the item at the ( character.
        choice = choices[i]
        parts = choice.split('(')
        # Extract the second part of the split (contains the ranking and closing parenthesis).
        ranking_part = parts[1]
        # Remove the closing parenthesis from the ranking part.
        ranking = ranking_part[:-1]

        # Same process, but for the next item
        choice_next = choices[i + 1]
        parts_next = choice_next.split('(')
        ranking_part_next = parts_next[1]
        ranking_next = ranking_part_next[:-1]

        # VERY important. Funky stuff happens if you compare the numbers as strings.
        if (int(ranking) > int(ranking_next)):
            print("Sorry! You lose, since " + choices[i] + " has a larger rank than " + choices[i + 1] + ".")
            print("Try again!")
            return False
    return True

def main():
    # FIFA Men's World Ranking as of 21 September 2023.
    URL = "https://en.wikipedia.org/wiki/Module:SportsRankings/data/FIFA_World_Rankings"
    rankings = dict()
    scrape(URL, rankings)

    choices = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]

    print("Credits to Austin Krance on TikTok for the game idea! You will be given 10 countries, try to rank them the best you can. If you want to end the game, enter \"exit\" or \"quit\"")
    print()

    hints = False
    hint_toggle = input("Press H if you want to play with hints. Otherwise, press anything else.\n")

    if (hint_toggle == "H"):
        hints = True
    print()

    for i in range(10):
        size = len(rankings)
        random_country = random.choice(list(rankings.keys()))
        random_rank = rankings[random_country]

        # You can't pick the same country more than once.
        del rankings[random_country]

        print("Your country is " + random_country + ". Pick a place to rank it.")

        # The hint system assumes an ideal world, e.g. Uruguay would usually
        # be the pick for #1. Unfortunately, reality isn't always this pretty.
        if (hints):
            x = size/10
            hint = round(float(random_rank)/x)
            if (hint == 0):
                hint = 1
            print("Hint: " + str(hint))
        print(choices)

        # dummy default invalid choice
        choice = "E"

        # The choice has to be an int.
        # The choice has to be from 1 to 10.
        # The choice must go in an empty slot, marked by X.
        while (not (choice.isdigit()) or not (1 <= int(choice) <= 10) or not (choices[int(choice) - 1] == 'X')):
            choice = input()
            # Printing error messages
            if choice.isdigit():
                if (int(choice) > 10):
                    print("Your number is too high! Pick a number from 1 to 10.")
                elif (choices[int(choice) - 1] != 'X'):
                    print("You already picked this slot!")
            else:
                if (choice.lower() == "quit" or choice.lower() == "exit"):
                    print("Better luck next time.")
                    exit()
                print("Invalid input! Pick a number from 1 to 10.")           
        choices[int(choice) - 1] = random_country + (" (") + str(random_rank) + (')')
    
    # Print final results
    print()
    print(choices)
    print()

    # Check to see if you won
    if win(choices):
        print("You won! Great job!")

if __name__ == "__main__":
    main()