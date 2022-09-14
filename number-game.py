from random import randrange


actual_number = randrange(1, 10)

for round in range(3):
    guess = int(input("please guess one number: "))
    if guess > actual_number :
        print("your guess is more than number")
    elif guess < actual_number :
        print( "your guess is less than number")

    else :
        print ("you win")
        
