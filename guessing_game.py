import random


# randomise the list
def shuffle_list():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]


# get player input
def player_input():
    return input('Guess the 3 digit number: ')


# check player input is correct or not
def is_correct(guess_numbers, shuffled_nums_list):
    current_num_list = [int(i) for i in guess_numbers]

    if current_num_list == shuffled_nums_list:
        match_val = 'Correct'
    elif current_num_list[0] == shuffled_nums_list[0] or current_num_list[1] == shuffled_nums_list[1] or \
            current_num_list[2] == shuffled_nums_list[2]:
        match_val = 'Close'
    elif current_num_list[0] in shuffled_nums_list \
            or current_num_list[1] in shuffled_nums_list \
            or current_num_list[2] in shuffled_nums_list:
        match_val = 'Match'
    else:
        match_val = 'Nope'
    return match_val


def play_game():
    print('Welcome to Code Breaker')
    playing = True
    shuffled_digits = shuffle_list()
    print(shuffled_digits)

    while playing:
        guess_digits = player_input()
        did_win = is_correct(guess_digits, shuffled_digits)
        print(did_win)

        if did_win is 'Correct':
            print('You are correct')
            playing = False


play_game()
