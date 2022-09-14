#driver code
from eight_puzzle import Puzzle
import numpy as np


#the starting configuration
#getting correct output for this###########################
#9 levels, 20 states generated, 10 explored
start = np.array([[2,4,3] , [1,6,8] , [7,5,0]])
r = 2
c = 2
goal = np.array([[1,2,3] , [4,5,6] , [7,8,0]])
rg = 2
cg = 2


#no output for this##############################################
start1 = np.array([[1,2,0] , [4,5,3] , [7,8,6]])
r1 = 2
c1 = 1
#same goal


#11 levels, no output
start2 = np.array([[2,4,3] , [1,0,8] , [7,6,5]])
r2 = 1
c2 = 1
#same goal


#trying aryans example
start4 = np.array([[2,8,1] , [0,4,3] , [7,6,5]])
r4 = 1
c4 = 0
goal4 = np.array([[1,2,3] , [8,0,4] , [7,6,5]])
rg4 = 1
cg4 = 1

#create the puzzle
#puz = Puzzle(start4, r4, c4, goal4, rg4, cg4)
puz = Puzzle(start, r, c, goal, rg, cg)

#solve
puz.solve()