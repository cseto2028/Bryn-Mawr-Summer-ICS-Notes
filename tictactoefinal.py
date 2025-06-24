board= [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]   
def printBoard(grid):
    for row in grid: 
        print("|", end = " ")
        for number in row: 
            print(number, end = "|")
        print()

def checkWinner(current_player, board): 
    if board [0] [0] == board [1][1] == board [2][2] == current_player: 
        print(f"Player {current_player} wins left diagonally!")
        return True

    for i in range(len(board)): 
        if board[i][0] == board[i][1] == board[i][2] == current_player: 
            print(f"Player {current_player} wins with a row victory!")
            return True
        
    for i in range(len(board)): 
        if board[0][i] == board [1][i] == board [2][i] == current_player: 
            print(f"Player {current_player} wins with a column victory!")
            return True
        
    if board [0][2] == board [1][1] == board [2][0] == current_player: 
            print(f"Player {current_player} wins right diagonally!")
            return True
def switchPlayer(current_player): 
     if current_player == "X": 
          return "O"
     if current_player == "O": 
          return "X"

def main(): 
     board= [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ]
     player= "O"
     check= True 
     while check == True: 
        print(f"{player}'s turn")
        printBoard(board)
        row= int(input("Enter the row you want to place your piece: "))
        col= int(input("Enter the column you want to place your piece: "))
        board[row][col] = player 
        if checkWinner(player, board) == True: 
            check= False
        player= switchPlayer(player)


main ()
