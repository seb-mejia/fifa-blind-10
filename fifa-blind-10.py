from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

def womens_scrape(URL, womens_rankings):
    soup = BeautifulSoup(urlopen(URL), "html.parser")
    span_elements = soup.find_all("span", class_="s2")
    country_rank = 1

    # Only items 5 through 197 are countries
    for span in span_elements[5:197]:
        country_name = span.text.strip('"')
        womens_rankings[country_name] = country_rank
        country_rank += 1

def mens_scrape(URL, mens_rankings):
    soup = BeautifulSoup(urlopen(URL), "html.parser")
    span_elements = soup.find_all("span", class_="s2")
    country_rank = 1

    # Only items 8 through 215 are countries
    for span in span_elements[7:214]:
        country_name = span.text.strip('"')
        mens_rankings[country_name] = country_rank
        country_rank += 1

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
    # As of 25 January 2024, this looks like it's still up to date.
    mens_URL = "https://en.wikipedia.org/wiki/Module:SportsRankings/data/FIFA_World_Rankings"
    mens_rankings = dict()
    mens_scrape(mens_URL, mens_rankings)

    womens_URL = "https://en.wikipedia.org/wiki/Module:SportsRankings/data/FIFA_Women%27s_World_Rankings"
    womens_rankings = dict()
    womens_scrape(womens_URL, womens_rankings)

    # You'd have to check all 10! board combinations for combined. Maybe let's not.
    '''
    combined_rankings = dict()

    for country in set(mens_rankings.keys()).union(set(womens_rankings.keys())):
        # If the country isn't available, set its rank to the maximum possible value
        mens_rank = mens_rankings.get(country, float("inf"))
        womens_rank = womens_rankings.get(country, float("inf"))

        combined_rankings[country] = min(mens_rank, womens_rank)
    '''

    print("Credits to Austin Krance on TikTok for the game idea! You will be given 10 countries, try to rank them the best you can. If you want to end the game, enter \"exit\" or \"quit\"\n")

    # dummy default invalid mode
    mode = "E"
    print("Press M to play with men's rankings, or W to play with women's rankings.")
    while (mode not in ["M", "W"]):
         mode = input()
         if (mode.lower not in ["m", "w", "M", "W"]):
            print("Press M to play with men's rankings, or W to play with women's rankings.")

    if (mode in ["m", "M"]):
        rankings = mens_rankings
    elif (mode in ["w", "W"]):
        rankings = womens_rankings

    hints = False
    hint_toggle = input("Press H if you want to play with hints. Otherwise, press anything else.\n")

    if (hint_toggle in ["h", "H"]):
        hints = True
    print()

    choices = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]

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
                elif (int(choice) == 0):
                    print("Your number is too low! Pick a number from 1 to 10.")
                elif (choices[int(choice) - 1] != 'X'):
                    print("You already picked this slot!")
            else:
                if (choice == ""):
                    print("Please provide an input!")
                elif (choice.lower() == "quit" or choice.lower() == "exit" or choice.lower() == "stop"):
                    print("Better luck next time, feel free to try again!")
                    exit()
                elif (choice[0] == "-" and choice[1:].isdigit()):
                    print("Your choice is too low! Pick a number from 1 to 10.")
                else:
                    print("Invalid input! Pick a number from 1 to 10.")           
        choices[int(choice) - 1] = random_country + (" (") + str(random_rank) + (')')
    
    print("\n", choices, "\n")

    if win(choices):
        print("You won! Great job!")

if __name__ == "__main__":
    main()
