#driver code
from eight_puzzle import Puzzle
import numpy as np


#the starting configuration
start = np.array([[1,2,3] , [0,4,6] , [7,5,8]])

#index of empty tile
r = 1
c = 0

#create the puzzle
puz = Puzzle(start, r, c)

#solve
puz.solve()