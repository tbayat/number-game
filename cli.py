from random import randrange
import argparse
import sys
from game import game
from utils import take_a_number_input

def get_arguments():
    parser = argparse.ArgumentParser(description="it is a number game")
    parser.add_argument('--start','-s', type = int, default=0)
    parser.add_argument('--end', '-e', type = int, default = 10)
    parser.add_argument('--rounds', '-r', type = int, default=3)

    return parser.parse_args()

def main():
    args = get_arguments()

    option = take_a_number_input("How many players are playing: ")

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

if __name__ == "__main__":
    main()
