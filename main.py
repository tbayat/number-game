from random import randrange
import argparse
import sys


parser = argparse.ArgumentParser(description="it is a number game")
parser.add_argument('--start','-s', type = int, default=0)
parser.add_argument('--end', '-e', type = int, default = 10)
parser.add_argument('--rounds', '-r', type = int, default=3)

def take_guess(count,player):
    try:
        guess = int(input(f"{count}> player {player} > please guess one number: "))
    except ValueError:
        return take_guess(count)
    return guess

def game_round(actual_number, round_number, player_name):
    guess = take_guess(round_number, player_name)

    won = False
    if guess > actual_number:
        print("your guess is more than number")
    elif guess < actual_number :
        print( "your guess is less than number")
    else:
        won = True

    return won

def game(number_of_players, number_of_rounds, range_start=0, range_end=10):
    actual_number = randrange(range_start, range_end)
    results = {}

    for round in range(1, number_of_rounds + 1):
        for player in range(1, number_of_players + 1):
            results[player] = game_round(actual_number, round, player)
        if any(results.values()):
            break

    return results, actual_number


def main():
    args = parser.parse_args()

    option =int(input("How many players are playing: "))

    if args.start >= args.end :
        print("the value for start should be less than end value")
        sys.exit(1)

    if args.rounds <= 0 :
        print("value of rounds should not be zero or negative")
        sys.exit(2)

    result, actual_number = game(option, args.rounds, args.start, args.end)
    print(f"Actual number was {actual_number}")
    for player, won in result.items():
        if won:
            print(f"player {player} won!")
        else:
            print(f"player {player} lost!")

main()
