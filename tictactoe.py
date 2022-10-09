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
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " " )
    print("   |   |   ")
    print("------------")

    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " " )
    print("   |   |   ")
    
printBoard(board)
print(isWinner(board,' '))