import random


def place_marker(board, marker, position):
    board[position] = marker


def display_board(board: list):
    print('\n' * 5)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' * 6)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 6)
    print(board[1] + '|' + board[2] + '|' + board[3])
    return board


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Which marker would you like to use? X or O: ')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def win_check(board, marker):
    markers_in_a_row = list(marker * 3)

    # different way of calculating it
    if board[7:10] == markers_in_a_row:
        won = True
        print('You\'ve won horizontally in the first row')
    elif board[4:7] == markers_in_a_row:
        won = True
        print('You\'ve won horizontally in the second row')
    elif board[1:4] == markers_in_a_row:
        won = True
        print('You\'ve won horizontally in the last row')
    elif board[1::3] == markers_in_a_row:
        won = True
        print('You\'ve won vertically in the first column')
    # bunch checking each board item
    elif board[2] == board[5] == board[8] == marker:
        won = True
        print('You\'ve won vertically in the second column')
    elif board[3] == board[6] == board[9] == marker:
        won = True
        print('You\'ve won vertically in the last column')
    elif board[1] == board[5] == board[9] == marker:
        won = True
        print('You\'ve won digonally upwards')
    elif board[7] == board[5] == board[3] == marker:
        won = True
        print('You\'ve won digonally downwards')
    elif full_board_check(board):
        won = False
        print('Tie')
    else:
        won = False
    return won


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    num_chosen = 0
    while num_chosen not in range(1, 10) or not space_check(board, num_chosen):
        num_chosen = int(input('Choose a position (1-9): '))

    return num_chosen


def choose_first():
    number = random.randint(0, 1)
    if number == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def replay():
    will_replay = input('Do you want to replay the game. Y or N: ')
    return 'y'.lower() in will_replay


def play_game():
    print('Welcome to Tic Tac Toe')
    # TUPLE UNPACKING - SIMILAR TO DESTRUCTURING
    player1_marker, player2_marker = player_input()
    playing = False
    current_board = [' '] * 10
    current_player_marker = player1_marker

    player_did_win = False

    if current_player_marker is not None:
        print(f'Player 1 is {player1_marker}\nPlayer 2 is {player2_marker}')
        print('Started playing')
        playing = True
        display_board(current_board)

    while playing:
        position = player_choice(current_board)
        place_marker(current_board, current_player_marker, position)
        display_board(current_board)
        # check for winner
        if win_check(current_board, current_player_marker):
            if current_player_marker == player1_marker:
                print('Player 1 wins')
                player_did_win = True
            else:
                print('Player 2 wins')
                player_did_win = True

        # make sure the players alternate every turn
        if not player_did_win:
            if current_player_marker == player1_marker:
                current_player_marker = player2_marker
                print('Player 2\'s turn')
            else:
                current_player_marker = player1_marker
                print('Player 1\'s turn')

        if player_did_win:
            will_replay = replay()
            if will_replay:
                play_game()
            else:
                quit()


play_game()
