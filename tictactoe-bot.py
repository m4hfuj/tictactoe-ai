player = 'O'
bot = 'X'
board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}

def printBoard():
    print()
    print("  "+board[7]+"|"+board[8]+"|"+board[9])
    print(" --+-+--")
    print("  "+board[4]+"|"+board[5]+"|"+board[6])
    print(" --+-+--")
    print("  "+board[1]+"|"+board[2]+"|"+board[3])
    print()

def isFree(pos):
    if board[pos] == ' ':
        return True
    else:
        return False 

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False

def checkWinFor(letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == letter:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == letter:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == letter:
        return True
    else:
        return False

def insertLetter(letter, pos):
    if isFree(pos):
        board[pos] = letter
        printBoard()
        if checkWin():
            print("*"*20)
            if letter == player:
                print('You WIN!!!')
                print("*"*20)
                exit()
            elif letter == bot:
                print('Bot WINS!!!')
                print("*"*20)
                exit()
        elif checkDraw():
            print("*"*20)
            print('DRAW!!!')
            print("*"*20)
    else:
        if letter == player:
            print('Space not Free....')
            choice = int(input('Enter new position: '))
            insertLetter(letter, choice)
            return
        elif letter == bot:
            return

def playerMove():
    pos = int(input("Enter position: "))
    insertLetter(player, pos)
    return

#--- Minimax Alogorithm ---#
def minimax(board, depth, isMaximizing):
    if checkWinFor(bot):
        return 10
    if checkWinFor(player):
        return -10
    if checkDraw():
        return 0
    
    if isMaximizing:
        maxScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth+1, False)
                board[key] = ' '
                if score > maxScore:
                    maxScore = score
        return maxScore
    
    else:
        minScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth+1, True)
                board[key] = ' '
                if score < minScore:
                    minScore = score
        return minScore

def botMove():
    print('Bot to move....')
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)
    return



print("The board: \n")
print("  7|8|9")
print(" --+-+--")
print("  4|5|6")
print(" --+-+--")
print("  1|2|3")
print()
print("Player to move first.... ")
print("Good Luck!")
while not checkWin() or checkDraw():
    playerMove()
    botMove()
