def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (1-3) for " + player + ": "))
        col = int(input("Enter column (1-3) for " + player + ": "))
        if (board[row-1][col-1] != " "):
            print("Invalid move. Try again.")
            continue
        board[row-1][col-1] = player
        if (check_win(board, player)):
            print_board(board)
            print("Player " + player + " wins!")
            break
        if (player == "X"):
            player = "O"
        else:
            player = "X"
    print("Thanks for playing!")

tic_tac_toe()