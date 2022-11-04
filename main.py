from IPython.display import clear_output
import random


# Function to display the board
def display_board(board):
    clear_output()

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# Function to choose player marker
def player_input():
    while 1:
        marker = input("Please choose your marker: ")

        if marker in ['X', 'O']:
            break
        else:
            print("Please choose a valid marker!")

    print(f'You have chosen {marker}!')
    return marker


# Function to put the marker on the board
def place_marker(board, marker, position):
    board[position] = marker


# Function to check if the game was won
def win_check(board, mark):
    win = False
    check = [mark, mark, mark]

    # Check lines
    for i in range(1, 7, 3):
        if board[i:i + 3] == check:
            win = True

    # Check columns
    for i in range(1, 4):
        if board[i:i + 7:3] == check:
            win = True

    # Check diagonals
    if board[1:10:4] == check or board[3:8:2] == check:
        win = True

    return win


# Function to randomly decide which player goes first
def choose_first():
    return random.randint(1, 2)


# Function to check if a position on board is available
def space_check(board, position):
    return board[position] == ' '


# Function to check if the board is full
def full_board_check(board):
    for place in board:
        if place == ' ':
            return False

    return True


# Function to ask for a player's next position
def player_choice(board):
    while 1:
        pos = int(input("Choose your position: "))

        if pos in [i for i in range(1, 10)]:
            if space_check(board, pos):
                return pos
            else:
                print("Position is not available!")
        else:
            print("Please choose a number between 1 and 9!")


# Function to check if the players what to play again
def replay():
    decision = input("Do you want to play again?(N/Y) ")

    while decision not in ['Y', 'y', 'N', 'n']:
        decision = input("Do you want to play again?(N/Y) ")

    return decision.lower() == 'y'


# Function that plays the game
def game():
    clear_output()
    print('Welcome to Tic Tac Toe!')

    board = ['$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = ['$', '', '']

    turn = choose_first()

    print(f'Player {turn} is first!')
    players[turn] = player_input()

    if players[turn] == 'X':
        players[len(players) - turn] = 'O'
    else:
        players[len(players) - turn] = 'X'

    print(f'Player 1 chose {players[1]}')
    print(f'Player 2 chose {players[2]}')
    print('\n')

    print("Game starts:")
    display_board(board)

    while not full_board_check(board):
        print(f"Player {turn}'s turn!")
        position = player_choice(board)
        place_marker(board, players[turn], position)

        display_board(board)

        if win_check(board, players[turn]):
            print("GAME OVER!")
            print(f'Player {turn} won!')
            return

        turn = len(players) - turn

    if win_check(board, players[turn]):
        print(f'Player {turn} won!')
    else:
        print("GAME OVER!")
        print("Neither one won!")


if __name__ == '__main__':
    game()

    while replay():
        game()
