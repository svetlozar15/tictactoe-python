#building the game board
gameBoard = ["*", "*", "*",
             "*", "*", "*",
             "*", "*", "*"]

def display_gameBoard():
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print(" - " + " - " + " - ")
    print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print(" - " + " - " + " - ")
    print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
#building the game board    
    
    
    
gameInProgress = True
gameWin = None
ongoingTurn = "X" 
    
def gamePlay(): # main func and loop
    display_gameBoard() # displaying the game board 
    
    while gameInProgress:
        
        gameTurn(ongoingTurn)
        
        gameOver()
        
        gameFlipTurn()
        
    # game end
    if gameWin == "X" or gameWin == "O":
        print(gameWin + " won!")
    elif gameWin == None:
        print("Tie.")
        
        
    
def gameTurn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1 - 9: ") # making your turn/move
    
    valid = False
    while not valid:
    
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: # input check/loop
            position = input("Invalid - choose from 1 - 9 again: ")
        
        position = int(position) - 1
        
        if gameBoard[position] == "*":
            valid = True
        else:
            print("Invalid - choose from 1 - 9 again: ")
        
    gameBoard[position] = player # displaying the result
    display_gameBoard()
    
    
def gameFlipTurn():
    global ongoingTurn
    
    if ongoingTurn == "X":
        ongoingTurn = "O"
    elif ongoingTurn == "O":
        ongoingTurn = "X"
    return

def gameOver():
    gameCheckWin()
    gameCheckTie()
    
def gameCheckWin():
    
    global gameWin
    
    rowWin = gameRow()
    columnWin = gameColumn()
    diagWin = gameDiagonal()
    if rowWin:
        gameWin = rowWin
    elif columnWin:
        gameWin = columnWin
    elif diagWin:
        gameWin = diagWin
    else:
        gameWin = None
    return

def gameCheckTie():
    if "*" not in gameBoard:
        gameInProgress = False
    return

def gameRow():
    global gameInProgress
    # row check
    row_1 = gameBoard[0] == gameBoard[1] == gameBoard[2] != "*"
    row_2 = gameBoard[3] == gameBoard[4] == gameBoard[5] != "*"
    row_3 = gameBoard[6] == gameBoard[7] == gameBoard[8] != "*"
    
    if row_1 or row_2 or row_3:
        gameInProgress = False
        
    if row_1:
        return gameBoard[0]
    elif row_2:
        return gameBoard[3]
    elif row_3:
        return gameBoard[6]
    return

def gameColumn():
    global gameInProgress
    # column check
    column_1 = gameBoard[0] == gameBoard[3] == gameBoard[6] != "*"
    column_2 = gameBoard[1] == gameBoard[4] == gameBoard[7] != "*"
    column_3 = gameBoard[2] == gameBoard[5] == gameBoard[8] != "*"
    
    if column_1 or column_2 or column_3:
        gameInProgress = False
        
    if column_1:
        return gameBoard[0]
    elif column_2:
        return gameBoard[1]
    elif column_3:
        return gameBoard[2]
    return

def gameDiagonal():
    global gameInProgress
    # diagonal check
    diag_1 = gameBoard[0] == gameBoard[4] == gameBoard[8] != "*"
    diag_2 = gameBoard[6] == gameBoard[4] == gameBoard[2] != "*"
    
    if diag_1 or diag_2:
        gameInProgress = False
        
    if diag_1:
        return gameBoard[0]
    elif diag_2:
        return gameBoard[2]
    return


gamePlay()
    
    