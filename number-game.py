from mimetypes import init
from random import randrange
import argparse
import sys


parser = argparse.ArgumentParser(description="it is a number game")
parser.add_argument('--start','-s', type = int, default=0)
parser.add_argument('--end', '-e', type = int, default = 10)
parser.add_argument('--rounds', '-r', type = int, default=3)

def take_guess(count):
    try:
        guess = int(input(f"{count}> please guess one number: "))
    except ValueError:
        return take_guess(count)
    return guess

def single_player(range_start = 0, range_end=10, rounds=3) :

    actual_number = randrange(range_start, range_end)
    won = False
    for count,round in enumerate(range(rounds),start=1):
        guess = take_guess(count)
        if guess > actual_number :
            print("your guess is more than number")
        elif guess < actual_number :
            print( "your guess is less than number")
        else :
            won = True
            break

    print (f"actual number was {actual_number}")
    return won


def main():

    args = parser.parse_args()
    if args.start >= args.end :
        print("the value for start should be less than end value")
        sys.exit(1)

    if args.rounds <= 0 :
        print("value of rounds should not be zero or negative")
        sys.exit(2)

    won = single_player(args.start, args.end , args.rounds)
    if won :
        print("you won")
    else :
        print("you lost")

main()
