from mimetypes import init
from random import randrange
import argparse
import sys


parser = argparse.ArgumentParser(description="it is a number game")
parser.add_argument('--start','-s', type = int, default=0)
parser.add_argument('--end', '-e', type = int, default = 10)
parser.add_argument('--rounds', '-r', type = int, default=3)

class player:
    def __init__(self, name, guess) :
        self.name = name
        self.guess = guess

def take_guess(count,player):
    try:
        guess = int(input(f"{count}> player {player} > please guess one number: "))
    except ValueError:
        return take_guess(count)
    return guess

def single_player(range_start = 0, range_end=10, rounds=3) :

    actual_number = randrange(range_start, range_end)
    won = False
    for count,round in enumerate(range(rounds),start=1):
        guess = take_guess(count,1)
        if guess > actual_number :
            print("your guess is more than number")
        elif guess < actual_number :
            print( "your guess is less than number")
        else :
            won = True
            break

    print (f"actual number was {actual_number}")
    return won

def two_player():
    winner_name2 = "noname"
    winner_name1 = "noname"
    looser_name1 = "noname"
    won = False
    actual_number = randrange(0, 50)
    p1 = player(input("player 1 > please enter your name:"),0)
    p2 = player(input("player 2 > please enter your name:"),0)
    for count, round in enumerate(range(5), start = 1):
        p1.guess = take_guess(count, 1)
        p2.guess = take_guess(count, 2)
        if p1.guess > actual_number and p2.guess > actual_number:
            print(f"{p1.name}'s guess is more than number")
            print(f"{p2.name}'s guess is more than number")
        elif p1.guess > actual_number and p2.guess < actual_number:
            print(f"{p1.name}'s guess is more than number")
            print(f"{p2.name}'s guess is less than number")
        elif p1.guess < actual_number and p2.guess > actual_number:
            print(f"{p1.name}'s guess is less than number")
            print(f"{p2.name}'s guess is more than number")
        elif p1.guess < actual_number and p2.guess < actual_number:
            print(f"{p1.name}'s guess is less than number")
            print(f"{p2.name}'s guess is less than number")
        
        elif p1.guess == actual_number and p2.guess == actual_number:
            won = True
            winner_name1 = p1.name
            winner_name2= p2.name
            break
        elif p1.guess == actual_number:
            won = True
            winner_name1 = p1.name
            looser_name1 = p2.name
            break
        else :
            won = True
            winner_name1 = p2.name
            looser_name1 = p1.name
            break
    print (f"actual number was {actual_number}")
    return [won, winner_name1, looser_name1, winner_name2]



def main():

    option =int(input("please choose 1 player or 2 player(just enter 1 or 2):"))
    if option == 1:
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
    else :
        result = two_player()
        won = result[0]
        if won == True and result[3] == "noname" :
            print(f"{result[1]} won and {result[2]} losed")
        elif won == True and result[3] != "noname" :
            print(f"{result[1]} and {result[3]} won")    
        else:
            print("both player were lose")
main()
