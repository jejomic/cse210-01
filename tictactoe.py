#For W01 Prove: Developer
#Author: Jeremiah Miclat


#variables
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
Win = 1
Draw = -1
Running = 0
Game = Running
Mark = 'X'


### FUNCTIONS ###

#main function
def main():
    gameRun()

#draws the board
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

#displays board keys
def DrawBoardKeys():
    print("Position Keys")
    print(" 1 | 2 | 3 " )
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")


#check if position is empty
def CheckPosition(x):
    if (board[x] == ' '):
        return True
    else:
        return False

#winning & draw patterns
def CheckWin():
    global Game
    # vertical pattern
    if (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    # horizontal pattern
    elif (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win

    # diagonal pattern
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
    # draw
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running

#starting the game
def gameRun():
    player = 1
    while (Game == Running):
        DrawBoard()
        
        if (player % 2 != 0):
            DrawBoardKeys()
            print("Player 1's chance")
            Mark = 'X'
        else:
            DrawBoardKeys()
            print("Player 2's chance")
            Mark = 'O'
        choice = int(
            input("Enter the position between [1-9] where you want to mark : "))
        if (CheckPosition(choice)):
            board[choice] = Mark
            player += 1
            CheckWin()
    if (Game == Draw):
        DrawBoard()
        print("Game Draw")
    elif (Game == Win):
        player -= 1
    if (player % 2 != 0):
        DrawBoard()
        print("Player 1 Won")
        input("Press enter to exit")
    else:
        DrawBoard()
        print("Player 2 Won")
        input("Press enter to exit")

#call main
main()