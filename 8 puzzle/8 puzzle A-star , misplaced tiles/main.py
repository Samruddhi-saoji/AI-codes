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



#10 levels, 105 states explored, 179 states generated
start2 = np.array([[2,8,1] , [0,4,3] , [7,6,5]])
r2 = 1
c2 = 0
goal2 = np.array([[1,2,3] , [8,0,4] , [7,6,5]])
rg2 = 1
cg2 = 1


#create the puzzles
puz2 = Puzzle(start2, r2, c2, goal2, rg2, cg2)
puz = Puzzle(start, r, c, goal, rg, cg)

#solve
#puz.solve()
puz.solve()