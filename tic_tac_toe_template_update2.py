"""tic_tac_toe"""


def create_board():
    """Prints an empty board. Provided for guidance, not necessary in this program.
    """
   
    print(" 0,0| 0,1| 0,2")
    print("----+----+----")
    print(" 1,0| 1,1| 1,2")
    print("----+----+----")
    print(" 2,0| 2,1| 2,2") 
    print ("Enter the the move for the current player\n")   
    
create_board() #The instruction key for the board player.

def print_board(board):
    print(board[0][0] + "|" + board[0][1] + '|' + board[0][2]) #The current playing board.
    print('-+-+-')
    print(board[1][0] + "|" + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + "|" + board[2][1] + '|' + board[2][2])




def check_winner(board, current_player): #Fuction for checking the winner in the board.

    if board[0][0] == board[0][1] == board[0][2] == current_player: #Across the top
        return True
    elif board[1][0] == board[1][1] == board[1][2] == current_player: #Across the middel
        return True
    elif board[2][0] == board[2][1] == board[2][2] == current_player: #Across the bottom
        return True
    elif board[0][0] == board[1][0] == board[2][0] == current_player: #Down on the left side
        return True
    elif board[0][1] == board[1][1] == board[2][1] == current_player: #Down in the middle
        return True
    elif board[0][2] == board[1][2] == board[2][2] == current_player: #Down on the left side
        return True
    elif board[0][2] == board[1][1] == board[2][0] == current_player: #Diagonal /
        return True
    elif board[2][2] == board[1][1] == board[0][0] == current_player: #Diagonal \
        return True
    
    else:
        return False
      

def update_board(board, row, col, current_player): #Function for updating the board.
    board[row][col] = current_player
    


def verify_entry(board, row, col): #Function for verifying the entry number.

    if 0 <= row and row <= 2 and 0 <= col and col <= 2: #Define the row and col
        if board[row][col] == " ": 
            return True

    else:
        return False
        


def play():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    print_board(board) #prints an empty board
    current = None
    moves = 0
    

    while (moves < 9 and not check_winner(board, current)): #game over?
    #play
        current = "X" if (current == None or current == "O") else "O"
        row, col = map(int, input("Enter the move for " + current +": ").split(","))
        while not verify_entry(board, row, col):
            print("Wrong entry. Think again!")
            row, col = map(int, input("Enter the move for " + current +": ").split(","))
        update_board(board, row, col, current)
        print_board(board) #prints the current board
        moves = moves + 1
   
    if moves < 9:
        print(current + " WON!")
        restart = input("Do want to play Again?(y/n)")#Restart(Y) or end(N) the game. 
        print("\nThanks for playing\n") #Will print at the end.
        if restart == "y" or restart == "Y": #Press y and enter to restart.
            if restart == "n" or restart == "N": " " #Press n and/or enter to quit.
    
            play()

    else: #If board the is full its gonna be a Tie or X or O won by the last move.
        print("Its a tie or\nWon by the last move\nGame over") 
        restart = input("Do want to play Again?(y/n)") #Restart(Y) or end(N) the game. 
        print("\nThanks for playing\n") #Will print at the end.
        if restart == "y" or restart == "Y": #Press y and enter to restart.
            if restart == "n" or restart == "N": " " #Press n and/or enter to quit.
            
            play()

            
play()

# 2,2 1,1 0,2 1,2 1,0 2,0 0,1 0,0 2,1 
# Boardtest Tie number """
