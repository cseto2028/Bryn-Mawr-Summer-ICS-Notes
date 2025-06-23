board= [
    [".", ".", "X"],
    [".", "X", "."],
    ["X", ".", "."],
]   
for row in board: 
    print("|", end = " ")
    for number in row: 
        print(number, end = "|")
    print()
current_player= "X" 
if board [0] [0] == board [1][1] == board [2][2] == current_player: 
        print(f"Player {current_player} wins left diagonally!")
for i in range(len(board)): 
    if board[i][0] == board[i][1] == board[i][2] == current_player: 
        print(f"Player {current_player} wins with a row victory!")
#for column problem, use for in loop 
#for right diagonal, use if statement 
for i in range(len(board)): 
     if board[0][i] == board [1][i] == board [2][i] == current_player: 
         print(f"Player {current_player} wins with a column victory!")
if board [0][2] == board [1][1] == board [2][0] == current_player: 
        print(f"Player {current_player} wins right diagonally!")
     
    
