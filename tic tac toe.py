#for displaying the board
def display_board(board):
    print('\n'*1)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print("------")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("------")
    print(board[7]+'|'+board[8]+'|'+board[9])

#for entering the player input
def player_input():

    marker=''
    #To check wheather whether user is entering the corect value
    while marker !='x' and marker !='o':
        marker=input("choose x or o")
    #Assigning the values to the player


    if marker=='x':
        return('x','0')
    else:
        return('o','x')
#adding user entered marker to the position
def place_marker(board, marker, position):

    #for choosing a position where to input
    board[position]=marker
#for checking the user whether the user win in 8 conditions
def win_check(board, mark):

    return((board[1]==board[2]== board[3]==mark)or# across the top
           (board[4]==board[5]==board[6]==mark)or# across the middle
           (board[7]==board[8]==board[9]==mark)or #acrooss the bottom
           (board[1]==board[5]==board[9]==mark)or # down the middle
           (board[1]==board[4]==board[7]==mark)or #down the middle
           (board[3]==board[6]==board[9]==mark)or #down the right side
           (board[3]==board[5]==board[7]==mark)or #diagonal
           (board[2]==board[5]==board[8]==mark))  #diagonal

#for random selecting the user for playing
import random

def choose_first():

    if random.randint(0,1)==0:
        return "player 1 "
    else:
        return "player 2"

def space_check(board, position):

    return board[position]==" "

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#for checking the user input the correct range
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position
#for asking the user want to play again
def replay():

    y=input('do you want to play again choose yes or no')
    if y.lower()[0]=='y':
        return position


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerchoice1, playerchoice2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, playerchoice1, position)

            if win_check(theBoard, playerchoice1):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, playerchoice2, position)

            if win_check(theBoard, playerchoice2):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break