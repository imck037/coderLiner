# tic tac toe game in python

import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

board = [" " for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("------------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

def isWinner(bo,le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        availableMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
        print("available positions are: ", availableMoves)
        move = input("Plese select a position to place'x' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Sorry, this space is occupied!")
                    speak.Speak("Sorry, this space is occupied!")
            else:
                print("please type a number within the range!")

        except:
            print("please type a number!")
            speak.Speak("please type a number!")
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print("Welcome to tic tac toe!")
    speak.Speak("Welcome to tic tac toe!")
    
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, computer won this time!")
            speak.Speak("Sorry, computer won this time!")
            break

        if not(isWinner(board, "X")):
            move = compMove()
            if move == None:
                break
            else:
                insertLetter("O", move)
                print("Computer placed an 'O' in position ", move)
                printBoard(board)
        else:
            print("you won! Good Job!")
            speak.Speak("you won! Good Job!")
            break
        

    if isBoardFull(board):
        if not(isWinner(board, "X")):
            print("Tie game!")
            speak.Speak("Tie game!")

main()

while True:
    speak.Speak("did you want to play again?")
    ans = input("Play again?(y/n): ")
    board = [" " for x in range(10)]
    if ans == "y":
        
        main()
    else:
        break


