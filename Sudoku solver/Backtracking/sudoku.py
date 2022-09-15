#using backtracking

import numpy as np

class Sudoku:
    #constructor
    def __init__(self, start) :
        self.board = start
        #board = 9x9 numpy matrix

        #print the start state
        print("The puzzle is: ")
        print(start)

        print("\nAll possible solutions to the problem are:")
        self.solve()

        #coming here means all the cells have been filled
        #print the final answer 
        #print("\nThe answer is: ")
        #print(self.board)


    #0 --> the cell hasnt been filled
    #retruns ALL POSSIBLE solutions
    def solve(self) :
        #for each cell on the board
        for row in range (0,9) :
            for col in range(0,9) :
                #if the cell is empty
                if  self.board[row][col] == 0:
                    #try putting each possible number from 1 to 9
                    for num in range (1,10) :
                        if self.isValid(row, col, num) :
                            #fill the cell with num 
                            self.board[row][col] = num

                            #recursive call
                            #continue solving furthur
                            self.solve()

                            #coming here means filling cell with num 
                            #created problems
                            #so clear the cell and try again
                            self.board[row][col] = 0

                    return

        #coming here means all the cells have been filled
        #print the final answer 
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




