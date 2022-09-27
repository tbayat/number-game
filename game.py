from random import randrange
from utils import take_a_number_input

# TODO this function is only useful for the CLI input scenario. It
# might be better to extract it as an abstract requirement of the
# final game module.
def take_guess(count, player):
    return take_a_number_input(f"{count}> player {player} > please guess one number: ")

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
