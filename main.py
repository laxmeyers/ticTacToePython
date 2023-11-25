from helpers import drawBoard, checkTurn, checkWin
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8:'8', 9:'9'}

playing = True
complete = False
turn = 0
previousTurn = -1
while playing:
    # reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    drawBoard(spots)
    if previousTurn == turn:
        print("Invalid spot selected, pick another spot.")
    previousTurn = turn
    print(f"Player {checkTurn(turn + 1)}'s turn: pick your spot or press 'q' to quit")

    choice = input()
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = checkTurn(turn)
    
    if checkWin(spots): playing, complete = False, True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
drawBoard(spots)

if complete:
    if checkTurn(turn) == 'X': print("X wins!")
    else: print("O wins!")
else:
    print("No winners :(")

print("Thanks for Playing")
        

