### the node class
import numpy as np


class Node :
    #goal board
    goal = np.array([[0,0,0], [0,0,0], [0,0,0]]) #default board

    #attributes
    board = np.array([[0,0,0], [0,0,0], [0,0,0]]) #default board 

    #child nodes: up , down, left, right
    parent = None #parent ref

    #hueristic values
    f = 0
    g = 0
    h = 0
    #f = g + h
        # g --> depth of node  #depth of root is 0
        # h ---> hueristic function  #misplaced tiles


    def __init__(self, board, r, c, move) :
        self.board = board

        #index of empty child
        self.r = r #row index
        self.c = c #col index

        #child nodes are initially null
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        #what move on the parent created this node?
        self.move = move
        # "Up" , "Down"  , "Left" , Right""


    #class methods
    #create child nodes
    def moveUp(self) :
        #if this board has been created by moving the empty tile down
        #then no point in creating the up child, as it will create the same board as its grandparent
        if self.move == "Down" :
            return None

        #if empty tile cannot be moved up, return null
        if self.r==0 :
            return None

        #create the child board
        #child borad is a copy of parent board
        child_board = np.copy(self.board)

        #move the empty tile up in the child board
        # self.r, self.c= index of the empty tile (0) on both child and parent board
        # to move up, exchnage (r,c) and (r-1,c) on child board
        child_board[self.r][self.c] = child_board[self.r - 1][self.c]
        child_board[self.r - 1][self.c] = 0
        #index of empty tile on child board = r-1, c

        #create the child node and add it to the tree
        child = Node(child_board, self.r - 1, self.c , "Up")
        child.parent = self
        self.up = child

        #set the hueristic values of the child
        child.g = self.g + 1
        child.h = child.getH()
        child.f = child.g + child.h      

        return child
    


    def  moveDown(self) :
        #if this board has been created by moving the empty tile up
        #then no point in creating the down child, as it will create the same board as its grandparent
        if self.move == "Up" :
            return None

        #if empty tile cannot be moved down, return null
        if self.r==2 :
            return None

        #create the child board
        #child borad is a copy of parent board
        child_board = np.copy(self.board)

        #move the empty tile down in the child board
        # self.r, self.c= index of the empty tile (0) on both child and parent board
        # to move down, exchnage (r,c) and (r+1,c) on child board
        child_board[self.r][self.c] = child_board[self.r + 1][self.c]
        child_board[self.r + 1][self.c] = 0
        #index of empty tile on child board = r+1, c

        #create the child node and add it to the tree
        child = Node(child_board, self.r + 1, self.c , "Down")
        child.parent = self
        self.down = child

        #set the hueristic values of the child
        child.g = self.g + 1
        child.h = child.getH()
        child.f = child.g + child.h

        return child



    def moveLeft(self) :
        #if this board has been created by moving the empty tile right
        #then no point in creating its left child
        if self.move == "Right" :
            return None
        
        #if empty tile cannot be moved left, return null
        if self.c==0 :
            return None

        #create the child board
        #child borad is a copy of parent board
        child_board = np.copy(self.board)

        #move the empty tile left in the child board
        #exchnage (r,c) and (r,c-1) on child board
        child_board[self.r][self.c] = child_board[self.r][self.c - 1]
        child_board[self.r ][self.c - 1] = 0
        #index of empty tile on child board = r, c-1

        #create the child node and add it to the tree
        child = Node(child_board, self.r, self.c-1 , "Left")
        child.parent = self
        self.left = child

        #set the hueristic values of the child
        child.g = self.g + 1
        child.h = child.getH()
        child.f = child.g + child.h 

        return child



    def moveRight(self) :
        #if this board has been created by moving the empty tile left
        #then no point in creating its right child
        if self.move == "Left" :
            return None

        #if empty tile cannot be moved right, return null
        if self.c==2 :
            return None

        #create the child board
        #child borad is a copy of parent board
        child_board = np.copy(self.board)

        #move the empty tile right in the child board
        #exchange (r,c) and (r,c+1) on child board   #board[r,c] = 0
        child_board[self.r][self.c] = child_board[self.r][self.c + 1]
        child_board[self.r ][self.c + 1] = 0
        #index of empty tile on child board = r, c+1

        #create the child node and add it to the tree
        child = Node(child_board, self.r, self.c + 1 , "Right")

        #parent child relation btw self node and child
        child.parent = self
        self.right = child

        #set the hueristic values of the child
        child.g = self.g + 1
        child.h = child.getH()
        child.f = child.g + child.h

        return child


    #hueristic function h(x) ######################################################################
    #misplaced tile
    def getH(self) :
        #goal = goal array
        count = 0

        for row in range(0,3) :
            for col in range(0,3) :
                #if self.board[row][col] !=  Node.goal[row][col] 
                #then tile is misplaced
                #exception = empty tile = 0
                if self.board[row][col] != 0:
                    if self.board[row][col] != Node.goal[row][col] :
                        count = count + 1

        return count




    #comparator function
    #compare 2 nodes
        # node1< node --> higher priority in Pqueue
    def __lt__(self, other) :
        #less f --> higher priority
        #tie breaker:
            #if same f, then node with lower h val has higher priority

        #if 2 nodes have same f val then compare h
        if self.f == other.f :
            if self.h < other.h :
                return True
        else : #compare f
            if self.f < other.f :
                return True
        return False



##############################################################################







    


    
    