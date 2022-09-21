#driver code
from eight_puzzle import Puzzle
import numpy as np


#the starting configuration
start = np.array([[2,4,3] , [1,6,8] , [7,5,0]])
r = 2
c = 2

#create the puzzle
puz = Puzzle(start, r, c)

#solve
puz.solve()