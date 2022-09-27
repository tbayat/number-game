
def take_a_number_input(message):
    try:
        return int(input(message))
    except ValueError:
        return take_a_number_input(message)
