board={
       1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" ",
       }
def printBoard(board):       
        print(board[1],"|",board[2],"|",board[3])    
        print("---------")
        print(board[4],"|",board[5],"|",board[6])    
        print("---------")
        print(board[7],"|",board[8],"|",board[9])
        print("\n")
play={
        1:"Player 1 VS Player 2",
        2:"Player 1 VS Comp"
        }

def spaceIsFree(position):
    
    if board[position]==" ":
        
        return True
    else:
        
        return False
 
    
def insertLetter(letter, position):
    if spaceIsFree(position):   
        board[position] =letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if  checkForWin():
            if letter=='X':
                
                if choice==1:
                    print("Player 1 wins !")
                    exit()
                elif choice==2:
                    
                    print("Bot wins !")
                    exit()
            else :               
                print("Player2 wins !")
                exit()
        return        

    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return
        
def checkDraw():
    for key in board.keys():
        if board[key]==" ":
            return False
    return True      


def checkForWin():
    if (board[1]==board[2] and board[1]==board[3] and board[1]!=" "):
        return True
    elif (board[4]==board[5] and board[4]==board[6] and board[4]!=" "):
        return True
    elif (board[7]==board[8] and board[7]==board[9] and board[7]!=" "):
        return True
    elif (board[1]==board[4] and board[1]==board[7] and board[1]!=" "):
        return True
    elif (board[2]==board[5] and board[2]==board[8] and board[2]!=" "):
        return True
    elif (board[3]==board[6] and board[3]==board[9] and board[3]!=" "):
        return True
    elif (board[1]==board[5] and board[1]==board[9] and board[1]!=" "):
        return True
    elif (board[3]==board[5] and board[3]==board[7] and board[3]!=" "):
        return True
    else:
        return False
 

def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

    
player1="O"
comp="X" 
player2="X"
def player1Move():
    position=int(input("Enter the position for'O' : "))
    insertLetter(player1, position)
    return

def player2Move():
    position=int(input("Enter the position for'X' : "))
    insertLetter(player2, position)
    return
def compMove():
    bestScore=-1000
    bestMove=0
    for key in board.keys():
        if board[key]==" ":
            board[key]=comp
            score=MiniMax(board, False)
            board[key]=" "
            if(score>bestScore):
                bestScore=score
                bestMove=key
                
    insertLetter(comp, bestMove)
    return


def MiniMax(board,isMaximizing):
    if checkWhichMarkWon(comp):
        return 1
    elif checkWhichMarkWon(player1):
        return -1
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore=-800
        for key in board.keys() :
            if(board[key]==" "):
                board[key]=comp
                score=MiniMax(board, False)
                board[key]=" "
                if(score>bestScore):
                    bestScore=score
        return bestScore  
                
    else :
         bestScore=800
         for key in board.keys():
             if board[key]==" ":
                 board[key]=player1
                 score=MiniMax(board, True)
                 board[key]=" "
                 if(score<bestScore):
                     bestScore=score
         return bestScore       
             
        
printBoard(board)

print("1:",play[1])
print("or")
print("2:",play[2])
choice=int(input("Please choose: 1 or 2 :"))
def choose ():
    
    if choice==1:
        while not checkForWin():       
            player1Move()
            player2Move()
    elif choice==2:
        
        print("Computer goes first ! Good Luck")
        while not checkForWin():
            
            compMove()
            player1Move()
    else: 
        print("Sorry")
        choose()
 
choose()
print("Positions are as follow")
print(1,2,3)
print(4,5,6)
print(7,8,9)
print("\n")

