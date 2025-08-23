'''Player:1 Is "X"
   Player:2 Is "O"'''


board = [
         ['0','1','2'],
         ['3','4','5'],
         ['6','7','8']
        ]

Player1 = input("Enter name for player 1: ")
Player2 = input("Enter name for player 2: ")

def print_board():
  for i in board:
    print(i)


def p1():
    n = int(input(f"{Player1}'s move (0-8): "))
    row, column = divmod(n, 3)
    if board[row][column] not in ['X', 'O']:  # Prevent overwriting
        board[row][column] = "X"
    else:
        print("Invalid move, try again.")
        p1()
    print_board()

def p2():
    n = int(input(f"{Player2}'s move (0-8): "))
    row, column = divmod(n, 3)
    if board[row][column] not in ['X', 'O']:  # Prevent overwriting
        board[row][column] = "O"
    else:
        print("Invalid move, try again.")
        p2()
    print_board()

def end():

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None  # means no winner still


print_board()
count = 0

for i in range(9):
    if i % 2 == 0:
        p1()
        winner = end()
        if winner == "X":
            print("Game Ended")
            print(f"{Player1} won!")
            break
    else:
        p2()
        winner = end()
        if winner == "O":
            print("Game Ended")
            print(f"{Player2} won!")
            break
    count += 1

if not end():
    print("Draw.")