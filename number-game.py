from random import randrange
import argparse


parser = argparse.ArgumentParser(description="it is a number game")
parser.add_argument('--start','-s', type = int, default=0)
parser.add_argument('--end', '-e', type = int, default = 10)
parser.add_argument('--rounds', '-r', type = int, default=3)
parser.add_argument('--count', '-c', type = int, default=3)

def single_player(range_start = 0, range_end=10, rounds=3, count=3) :

    actual_number = randrange(range_start, range_end)
    won = False
    for count,round in enumerate(range(rounds),start=1):
        guess = int(input(f"{count}> please guess one number: "))
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

    won = single_player(args.start, args.end , args.rounds , args.count)
    if won :
        print("you won")
    else :
        print("you lost")

main()


