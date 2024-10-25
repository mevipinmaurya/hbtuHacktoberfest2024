'''Player:1 Is "X"
   Player:2 Is "O"'''


board = [
         ['0','1','2'],
         ['3','4','5'],
         ['6','7','8']
        ]

def print_board():
  for i in board:
    print(i)


def p1():

  n = int(input("Jeevan's_move.  "))
  row = n//3
  column = n%3
  board[row][column]="X"
  print_board()

def p2():

  n = int(input("Thrishul's_move.  "))
  row = n//3
  column = n%3
  board[row][column]="O"
  print_board()

def end():
  if board[0][0]==board[1][0]==board[2][0]:
    return(board[0][0])

  elif board[0][1]==board[1][1]==board[2][1]:
    return(board[0][1])

  elif board[0][2]==board[1][2]==board[2][2]:
    return(board[0][2])


  elif board[0][0]==board[0][1]==board[0][2]:
    return(board[0][0])

  elif board[1][0]==board[1][1]==board[1][2]:
    return(board[1][1])

  elif board[2][0]==board[2][1]==board[2][2]:
    return(board[2][0])


  elif board[0][0]==board[1][1]==board[2][2]:
    return(board[0][0])

  elif board[0][2]==board[1][1]==board[2][0]:
    return(board[0][2])

  else:
    return("draw")




print_board()
count=0
for i in range(5):
  p1()
  count+=1
  a = end()
  if a=="X":
    print("Game Ended")
    print("Jeevan won")
    break
  if count==9:
    print("draw")
    break

  p2()
  count+=1
  a = end()
  if a=="O":
    print("Game Ended")
    print("Thrishul won")
    break
