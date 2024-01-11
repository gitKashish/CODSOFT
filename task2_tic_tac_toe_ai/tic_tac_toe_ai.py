# each cell of Tic-Tac-Toe board is indicated by an element of the list
# value of 0 : Empty cell
# value of 1 : Maximizing Player (AI)
# value of -1 : Minimizing Player (Human)
board = [0 for x in range(9)]

# Function to print Board
def print_board(board):
    temp_board = [' - ' for i in range(9)]
    for x in range(9):
        if(board[x] == 1):
            temp_board[x] = ' X '
        elif(board[x] == -1):
            temp_board[x] = ' O '
    for i in range(3):
        print(temp_board[i*3],' | ',temp_board[(i*3)+1],' | ',temp_board[(i*3)+2])

# Getting current state of a given board
# return value of 1 : Maximizing Player (AI) Won
# return value of -1 : Minimizing PLayer (Human) Won
# return value of 0 : Tie between both Players
# return value of None : Game is not yet terminated
def get_state(board):
    # Checking for Horizontal or Vertical Match
    for i in range(3):
        if(board[i*3] == board[(i*3)+1] == board[(i*3)+2] != 0):
            return board[i*3]
        elif(board[i] == board[i+3] == board[i+6] != 0):
            return board[i]
    # Checking for Diagonal match
    if(board[0] == board[4] == board[8] != 0 or board[2] == board[4] == board[6] != 0):
        return board[4]

    # Checking if any empty cell is left or not
    if (0 not in board):
        return 0
    else:
        return None    
        
# Minimax function to determine the best outcome from a position
def minimax(board, alpha, beta, isMax):
    # Return if position is terminating
    if(get_state(board) != None):
        return get_state(board)

    if(isMax): # Maximizing Player's best move
        best_val = float('-inf')
        for i in range(9):
            if(board[i]  == 0):
                temp_board = board.copy()
                temp_board[i] = 1
                eval = minimax(temp_board, alpha, beta, not isMax)
                alpha = max(eval, alpha)
                if(beta <= alpha):
                    break
                best_val = max(best_val, eval)
        return best_val
    else: # Minimizing Player's best move
        best_val = float('inf')
        for i in range(9):
            if(board[i]  == 0):
                temp_board = board.copy()
                temp_board[i] = -1
                eval = minimax(temp_board, alpha, beta, not isMax)
                beta = min(eval, beta)
                if(beta <= alpha):
                    break
                best_val = min(best_val, eval)
        return best_val

# Function to get the best possible move from the available moves
# This is a maximization evaluation function
def evaluate(board_given):
    best_val = float('-inf')
    best_move = 0
    for i in range(9):
        if(board_given[i] == 0): # Try every valid position
            temp_board = board_given.copy()
            temp_board[i] = 1
            eval = minimax(temp_board, float('-inf'), float('inf'), False)
            if(eval > best_val): # Store the move with best outcome (maximum)
                best_move = i
                best_val = eval
    return best_move

# Actual Game Interface
Max_turn = True # Give first turn to AI
# Loop continues until game is not in a terminating state
while(get_state(board) == None):
    if(Max_turn): # AI Move
        move = evaluate(board)
        print("AI Move : ",move)
        board[move] = 1
        print_board(board)
        Max_turn = not Max_turn
    else: # Human Move
        move = input("Choose Move : ")
        if(move == "quit"):
            break
        move = int(move)
        board[move] = -1
        print_board(board)
        Max_turn = not Max_turn

# Show Result
winner = "Game ended in a Tie!!"
if(get_state(board) == 1):
    winner = "AI Won!!"
elif(get_state(board) == -1):
    winner = "Human Won!!"

print("GAME OVER!!")
print(winner)
input("Press any key to exit")
