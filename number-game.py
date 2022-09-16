from random import randrange

def single_player() :

    actual_number = randrange(1, 10)
    won = False
    for round in range(3):
        guess = int(input("please guess one number: "))
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

    won = single_player()
    if won :
        print("you won")
    else :
        print("you lost")

main()


