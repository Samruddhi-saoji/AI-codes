from queue import PriorityQueue
import numpy as np

class Sudoku:
    oneval = [] #list of cells with only 1 possible value remaining
    #i --> ith cell 
    # oneval[i] = [r,c] = indexes of the ith cell 

    #list of cells whose value has been fixed
    fixedval = [] 
    #i --> ith cell 
    # oneval[i] = [r,c, num] = indexes of the ith cell , its value

    #priority queue of cells for backtracking
    pq = PriorityQueue()
        #priority = shorter rem_val list
        #element = (priority, (row, col))


     
    #constructor
    def __init__(self, start) :
        self.board = start
        #board = 9x9 numpy matrix
        #0 --> the cell hasnt been filled

        #list of remaining values
        self.remval = [[0 for x in range(9)] for y in range(9)]
        self.back_track_count = 0

        #print the start state
        print("The puzzle is: ")
        print(start)

        #solve
        self.solve()

        

    #solve
    def solve(self) :
        #initialise remval
        self.initialise_remval()
        #eliminate options from remval lists for all fixed cells
        self.eliminateAll()

        #fill all cells which have only 1 possible val
        i = 0 #index
        while i < len(self.oneval) :
            cell = self.oneval[i]  
            #indices of cell
            row = cell[0]
            col = cell[1]

            print(cell)
            print(self.remval[row][col])
            print(self.board)

            #only possible val
            #num = 1st element is list remval[row][col]
            num = self.remval[row][col][0]

            #fill cell
            self.fillCell(row, col,num)

            
            #increment value of i
            i=i+1

        #now there are no more cells that have only 1 possible val
        #check if all cellls have been filled
        if len(self.fixedval) != 81 :
            #now solve remaining by backtracking method
            print("Total cells fixed before starting backtracking = " , len(self.fixedval)) 

            print("\nThe answer is: \n")
            self.solve_by_backtracking()
            return
        else :
            #all cells have been filled
            #print the finished board
            print("\nThe answer is: \n")
            print(self.board)



    def initialise_remval(self) :
        #for each cell on the board
        for row in range (0,9) :
            for col in range(0,9) :
                #initalise rem_val list
                if  self.board[row][col] == 0:
                    self.remval[row][col] = [1,2,3,4,5,6,7,8,9]
                else:
                    #for fixed elements
                    # remval list is empty list
                    self.remval[row][col] = []

                    #add cell to list of fixed cells
                    val = self.board[row][col]
                    self.fixedval.append([row, col, val])

    

    #for fixed cells, remove that value form row, col and box
    def eliminate(self, row, col, num) :
        #board[row][col] has fixed value num

        #the entire row 
        for r in range(0,9) :
            #remval list = self.remval[r][col]
            #check if list contains num
            if num in self.remval[r][col] :
                self.remval[r][col].remove(num)

                #if the cell has only 1 possible option now
                #then add it to onerem list
                if len(self.remval[r][col]) == 1 :
                    self.oneval.append([r, col])

        #the entire col 
        for c in range(0,9) :
            #check if list contains num
            if num in self.remval[row][c] :
                self.remval[row][c].remove(num)

                #if the cell has only 1 possible option now
                #then add it to onerem list
                if len(self.remval[row][c]) == 1 :
                    self.oneval.append([row, c])

        #the entire box
        #for the given cell, the box is :
        start_row = (row//3)*3
        end_row = start_row + 2

        start_col = (col//3)*3
        end_col = start_col + 2

        #for each cell in the box
        for r in range(start_row, end_row+1) :
            for c in range(start_col , end_col + 1) :
                #check if list contains num
                if num in self.remval[r][c] :
                    #remove num from remval list
                    self.remval[r][c].remove(num)

                    #if the cell has only 1 possible option now
                    #then add it to onerem list
                    if len(self.remval[r][c]) == 1 :
                        self.oneval.append([r, c])

        

    #forward checking
    #for each cell whose value is fixed
    #remove the number from the remval list of all cells in the same row, col, box
    def eliminateAll(self) :
        for cell in self.fixedval :
            #indices of cell
            r = cell[0]
            c = cell[1]
            #value of cell
            num = cell[2]

            #eliminate options form row, col, box
            self.eliminate(r,c,num)



    def fillCell(self ,row,col,num) :
        #fill the cell(row,col) with the value num
        self.board[row][col] =num

        #add cell to list of fixed cells
        self.fixedval.append([row,col,num])

        #clear the remval list of this cell   
        self.remval[row][col] = []

        #eliminate num from remval of
        # all cells in the same row,col,box
        self.eliminate(row, col, num) 

        



    #retruns ALL POSSIBLE solutions
    def solve_by_backtracking(self) :
        #initialsie the priority queue
        self.pq.queue.clear()     #########################think of a better approach

        #add each empty cell to pq
        for row in range (0,9) :
            for col in range(0,9) :
                #if the cell is empty and cell not already in queue
                if  self.board[row][col] == 0 :
                    #add cell index to priority queu
                    self.pq.put(( len(self.remval[row][col]) , (row,col) ))
        
        #for each cell in order of priority
        while self.pq.empty() == False:
            tup = self.pq.get()
            r = tup[1][0] #row index of cell
            c = tup[1][1] #col index

            #solve by backtracking for cell [r][c]

            #try putting each val from remval list
            for num in self.remval[r][c]:
                if self.isValid(r, c, num) :
                    #fill the cell with num 
                    self.board[r][c] = num

                    #recursive call
                    #continue solving furthur
                    self.solve_by_backtracking()

                    #coming here means filling cell with num 
                    #created problems
                    #so clear the cell and try again
                    self.board[r][c] = 0
                    self.back_track_count = self.back_track_count + 1

            return

        #coming here means all the cells have been filled
        #print the final answer 
        print("Number of times backtracking was done: ",self.back_track_count)
        print(self.board)
        print()

        

    #will filling the cell (row, col) with number num 
    #voilate any constraints?
    def isValid(self,row, col, num)->bool :
        #given cell = mat[row][col]

        #check the entire row of the given cell
        for c in range (0,9) :
            if self.board[row][c] == num :
                #num appears in another cell of the given row
                #thus num cant be enterred in the given cell
                return False  

        #check the entire col of the given cell
        for r in range(0,9) :
            if self.board[r][col] == num:
                return False

        #check the entire box of the given cell
        #for the given cell, the box is :
        start_row = (row//3)*3
        end_row = start_row + 2

        start_col = (col//3)*3
        end_col = start_col + 2

        #check each cell in the box
        for r in range(start_row, end_row+1) :
            for c in range(start_col , end_col + 1) :
                if self.board[r][c] == num :
                    return False

        #if we reach here it means
        #num hasnt appeared in the given row, col or box
        #hence the move is valid
        return True


   