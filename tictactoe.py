board=[' ' for i in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def IsFreeSpace(pos):
    return board[pos]==' '

def IsBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True


def isWinner(b,l):
    return(b[1]==l and b[2]==l and b[3]==l)or (b[4]==l and b[5]==l and b[6]==l)or (b[7]==l and b[8]==l and b[9]==l) or (b[1]==l and b[4]==l and b[7]==l)or (b[2]==l and b[5]==l and b[8]==l)or (b[3]==l and b[6]==l and b[9]==l)or(b[1]==l and b[5]==l and b[9]==l)or(b[3]==l and b[5]==l and b[7]==l)


def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " " )
    print("   |   |   ")
    print("------------")

    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " " )
    print("   |   |   ")
    print("------------")

    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " " )
    print("   |   |   ")

def playerMove():
  run = True
  while run:
    move=input("Please select a position to enter the X                         between 1 to 9")
    try:

      move=int(move)
      if move>0 and move<10:
        if IsFreeSpace(move):
          run = False
          insertLetter('X',move)
          printBoard(board)
        else:
          print("The position is already occupied")
      else:
        print("Please enter a number between 1 and 9")    
    except:
      print("Please enter an integer")
      
      
    
printBoard(board)

playerMove()