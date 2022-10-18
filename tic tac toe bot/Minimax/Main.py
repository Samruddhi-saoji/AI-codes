import math
import random
import time


#the tic tac toe game class
class Game:
    #attributes
    human = None  #X or O
    bot = None #X or O

    bestMove = None #used in minimax function
    #value will be set in minimax


    def __init__(self) -> None:
        self.board = [" " for x in range (0,9)]
        self.winner = None

        #start playing
        self.play()


    #function to print the board
    #print the board
    def printBoard(self) :
        print()
        print(self.board[0] + "  |  " + self.board[1] + "  |  " + self.board[2])
        print("___  ___  ___")
        print()
        print(self.board[3] + "  |  " + self.board[4] + "  |  " + self.board[5])
        print("___  ___  ___")
        print()
        print(self.board[6] + "  |  " + self.board[7] + "  |  " + self.board[8])
        print()
        print()


    #function to check if game has been won
    #latest move: piece, cell
    #piece = X or O
    def isWinner(self, cell, piece) :
        #check the entire row of the cell #############
        #cell lies in the row:
        row_start = 3*math.floor(cell/3)
        row_end = row_start + 2

        #if each cell in row is filled with the piece, then piece wins
        if all( self.board[cel] == piece for cel in range(row_start, row_end +1)) :
            return True


        #check the entire col of the cell #############
        #cell lies in the col:
        col_mid = (cell%3) + 3
        col_indices = [col_mid - 3, col_mid, col_mid + 3]
        #list of the indices of each cell in the column

        #if each cell in col is filled with the piece, then piece wins
        if all( self.board[cel] == piece for cel in col_indices) :
            return True


        #check the diagonals
        #if the given cell lies on a diagonal, then we must check the diagonal too
        #cell lies on diagonal if cell index is even
        if cell%2 == 0 :
            #indices of the diagonal cells
            diag1 = [0, 4, 8]
            diag2 = [2, 4, 6]

            #check 1st diagonal
            if all( self.board[cel] == piece for cel in diag1) :
                return True

            #check 2nd diagonal
            if all( self.board[cel] == piece for cel in diag2) :
                return True


        #all possible combinations have been checked
        #piece has not won ye t
        return False


    #returns the number of empty cells on the board
    def emptyCells(self) :
        return self.board.count(" ")

    
    #returns a list of all possible moves
    def possibleMoves(self) :
        list = [] #list of indices of all empty cells

        for cell in range (0,9) :
            if self.board[cell] == " " :
                list.append(cell)

        return list


    #human players move
    #returns the cell index
    def humanMove(self) :
        cell = int(input("Enter cell number (0-8) : "))

        #if the enterred cell number is not btw 0-8, or if the cell is already occupied, raise error
        if cell not in self.possibleMoves() :
            print("Enter valid cell number. \n")
            return self.humanMove()
        else: #valid cell no.
            #fill the cell with the human piece
            self.board[cell] = self.human
            return cell


    #bot move
    #returns index of the cell
    def botMove(self) :
        #what cell to make the move in?
        #if the board is empty, ie if the bot is making the first move
        if self.emptyCells()==9 :
            #make a random move
            cell = random.randint(0,8)
        else: #its not the first move
            #minimax decides the optimal move
            self.minimax(self.bot)
            cell = self.bestMove

            #for debugging #######################################
            if cell == None :
                print("Error here")

        #make the actual move
        self.board[cell] = self.bot

        return cell


    #minimax algorithm
    #deciding the optimal move for bot
    #sets the value of self.bestmove
    #returns the utility score of the optimal move
    def minimax(self, player) :
        #player = whose turn it is #maybe bot or human
        #the other player
        '''if player == "X" :
            other = "O"
        else:
            other = "X" '''
        if player == self.human :
            other = self.bot
        else:
            other = self.human

        
        #check if previous move was the winning move
        if self.winner != None :
            #game over, return utility value
            #find win-factor
            if self.winner == self.bot:
                winf = 1
            else : #human wins
                winf = -1

            #utility score = winf x (empty cells + 1)
            utility = winf*(self.emptyCells() + 1)

            return utility
        #if previous move resulted in a tie
        if self.emptyCells() == 0 :
            #utility = winf = 0
            return 0

        
        #coming here means the game is still on
        #set the base utility score
        if player == self.human :
            best = math.inf
        else: #player = bot
            best = -math.inf
        #best = utility score of optimal move

        bestMove = None #the optimal move

        #try each possible move of player
        for move in self.possibleMoves() :
            self.board[move] = player
            #if this move resulted in a win
            if self.isWinner(move, player) == True :
                self.winner = player

            #now simulate the furthur game
            simScore = self.minimax(other) #play from opponents side
            #simscore = best utility score in the simulated game

            #undo the move
            self.board[move] = " "
            self.winner = None

            #if the utility score of the simulated game is better than the best utility score yet, then update the value of best
            #for bot, highest utility score is best
            #for human player, minimum is best
            if player == self.bot:
                if simScore > best :
                    best = simScore
                    #this move is the optimal move
                    bestMove = move
            else:  #player = human
                if simScore < best :
                    best = simScore
                    bestMove = move

        #coming here means all possible moves have been tried
        #all possible games have been stimulated
        self.bestMove = bestMove #the best move from all possible simulated games

        return best


    #actually playing the game
    def play(self) :
        print("X starts the game.")
        self.human = input("Choose your piece, X or O : ")

        #set bot a/c to human
        if self.human == "X" :
            self.bot = "O"
            #X starts
            player = self.human
        else: #human = O
            self.bot = "X"
            player = self.bot #X starts

        #while there are still empty cells on the board
        #each iteration = 1 turn/ 1 move
        while self.emptyCells() > 0 :
            #if its humans chance
            if player == self.human :
                print("Its your turn.")
                cell = self.humanMove()
            else: #bot's turn
                cell = self.botMove()

            #print the board
            self.printBoard()

            #check if this move resulted in a win
            if self.isWinner(cell, player):
                print(player + " wins!")
                return

            #coming here means game is still on
            #now switch player
            if player == self.human :
                player = self.bot
                #human just played, its bot's chance now
            else:
                #bot just played, its humans chance now
                player = self.human

            time.sleep(.4) #to create pause btw turns
            #otherwise game is too fast

        #all cells filled, butnobody won
        #its a tie
        print("Its a tie")



#driver code
game = Game()




    
