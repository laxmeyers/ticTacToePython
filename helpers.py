def drawBoard(spots):
    board = (f"{spots[1]}|{spots[2]}|{spots[3]}\n"
             f"{spots[4]}|{spots[5]}|{spots[6]}\n"
             f"{spots[7]}|{spots[8]}|{spots[9]}\n")
    print(board)

def checkTurn(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'

def checkWin(spots):
    # handle horizontal wins
    if(spots[1]==spots[2]==spots[3]) \
       or (spots[4] == spots[5] == spots[6]) \
       or (spots[7] == spots[8] == spots[9]):
        return True
    # handle the vertical wins
    elif (spots[1]==spots[4]==spots[7]) \
       or (spots[2] == spots[5] == spots[8]) \
       or (spots[3] == spots[6] == spots[9]):
        return True
    # handle diagnole wins
    elif (spots[1]==spots[5]==spots[9]) \
       or (spots[3] == spots[5] == spots[7]):
        return True
    # if no one has won
    else:
        return False