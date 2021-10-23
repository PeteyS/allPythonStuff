

def display(board):
    print ("                                        ") #create the outline for the tic tac game, the empty spaces are to create padding between the pre and post text
    print ("                                        ") #so the game is clearer
    print (board[7] + "|" + board[8] + "|" + board[9])
    print (board[4] + "|" + board[5] + "|" + board[6])
    print (board[1] + "|" + board[2] + "|" + board[3])
    print ("                                        ")
    print ("                                        ")


def play_first():

    who = False #a boolean for the first player choice, to make sure the choose an acceptable input

    while who == False:

        first = input("Player 1: Do you wish to be X or O (Enter X or O to choose): ") #does player 1 want to be x or o
        if first not in ["X","x","O","o"]:
            print("Please enter either X to use X or O to use O")
        elif first.upper() == "X":
            print ('Player 1 will be using X and Player 2 will be using O') #if player 1 chose x then player 1 will be x and player 2 will be o
        else:
            print ("Player 1 will be using O and Player 2 will be using X") #if player 1 chose o then player 1 will be o and player 2 will be x

        red = False #boolean for whether players want to change letters

        while red == False:
            ready = input("Do you wish to continue or do you wish to reselect which letter you will be using. Enter Y to continue or N to reselect: ")   #yes or no if they wanna change 
            if ready not in ["Y", "y", "N", 'n']:
                print ("Please enter Y for yes or N for no: ")
            elif ready.upper() == "Y": #if player is ready,exit both loops
                red = True
                who = True
            elif ready.upper() == "N": #if player is not ready, exit ready loop and go back to choice loop
                red = True
                who = False

        first = first.upper() #turn first into capital to make last if statement easier. Could've done it earlier but i didnt so im not going back to fix it

        if first == "O": #assigning player 2's variable depending on player 1's choice 
            second = "X"
        elif first == "X":
            second = "O"

    return first,second #return first and second choice

def game_check(board):
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9] or board[7] == board[4] == board[1] or board[8] == board[5] == board[2] or board[9] == board[6] == board[3] or board[1] == board[5] == board[9] or board [3] == board[5] == board[7]:
        return 1 #all the winning possible solutions. There is probably a better way to do this, didnt have the brain power to figure it out
    elif "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board: #for a draw, this seemed to be the easiest way, theres probably a more compact way to do this
        return 2


#need to make way of checking if player input spot is already taken. Use numbers instead of empty spaces, once a number is chosen remove it from list so if its chosen again, throw up error
def player_input(board,first,second):


    key = True #creating to booleans for the two while loops for each players input
    key1 = True

    while key == True: #player 1 loop 
        player_spot = input(f'Player 1: Enter where you want to place your {first} (1-9): ') #ask their input 
        if player_spot not in board or player_spot.upper() == 'X' or player_spot.upper() == "O" : #if user inputs something not on board or the letter x or o
            print ("Player 1: Please enter a number between 1-9 that is still on the board: ") #give em this message and make them enter a new value
        elif player_spot in board: #if input is in the board
            board[int(player_spot)] = first.lower() #change spot on board to the letter that first chose
            key = False #exit loop

    display(board) #display the board to improve game clarity
    print (board)

    if game_check(board) == 1: #check to see if player 1 won
        print (f'Player 1 has won using the letter {first}') #display message showing that player 1 won
        return board #return statement to exit function
    elif game_check(board) == 2: #check if game is a tie
        print ("Game is a tie")
        return board

    while key1 == True: #player 2 loop
        player_spot = input (f'Player 2: Enter where you want to place your {second} (1-9): ') #asking player 2 to input letter
        if player_spot not in board or player_spot.upper() == 'X' or player_spot.upper() == "O" : #see player 1 loop for rest of shit
            print ("Player 2: Please enter a number between 1-9 that is still on the board: ")
        elif player_spot in board:
            board[int(player_spot)] = second.lower()
            key1 = False
    
    print (board)

    if game_check(board) == True:#check first if statment game check
        print (f'Player 2 has won using the letter {second} ')
        return board
    elif game_check(board) == 2:
        print ("Game is a tie")
        return board

    return board #update board 


game_start = True #this is for the user interface

while game_start: #overarching loop over the whole game, reason is to reset board from the second while loop where its changed
    print ('\n' * 50) #print empty spaces for game clarity
    print ("Welcome to Tic Tac Toe")#obvious welcome message

    board = ['#','1','2','3','4','5','6','7','8','9',] #assinging the board
    board1 = board #dont even need this anymore but its too late
    game_on = True #boolean for the second while loop that holds the actual game logic

    first,second = play_first() #who wants to be what letter

    while game_on: #second while loop that holds game logic

        key_restart = True # variable used for restart loop below

        display(board1) #display board
        board1 = player_input(board1,first,second) #update board using player_input function

        if game_check(board1) == 1 or game_check(board1) == 2: #if someone has won or game has drawn
            while key_restart == True: #used to control restart while loop
                user_restart = input("Do you wish to play agian(Y/N): ") #ask user if they want to restart
                if user_restart.upper() not in ["Y","N"]: #if restart isnt Y or N ask agian
                    print ("Please enter Y for yes or N for no")
                elif user_restart.upper() == "Y": #if user wants to restart
                    key_restart = False #get out of restart while loop
                    game_on = False #get out of game logice loop
                    game_start = True #start at the top
                elif user_restart.upper() == "N": #if they dont want to restart
                    print ('Thanks for playing') #exit message
                    key_restart = False #bounce from the loops and end the program
                    game_on = False
                    game_start = False
                    

