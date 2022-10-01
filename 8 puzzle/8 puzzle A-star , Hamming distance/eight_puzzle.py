#solving the 8 puzzle problem with bfs
import numpy as np
from Node import Node #node class
from collections import deque #stack for printing answer
from queue import PriorityQueue #priority queue


class Puzzle :
    #attributes ###########################################
    #the starting state = root.board

    #the goal node
    goal_node:Node = None  #data type = Node

    #has goal node been generated?
    goal_found = False

    #total number of states generated
    states_generated = 0
    #total number of states explored
    states_explored = 0
    

    #constructor #######################
    #creates the root node of the puzzle
    def __init__(self, start, r, c, goal, rg, cg) :
        # start = numpy array of the starting board
        #(r,c) = index of empty tile on start board

        #create the root node
        self.root = Node(start, r, c, "Initial")
        self.root.parent = None
        self.states_generated = 1 

        self.g = 0

        #the goal state
        self.goal = goal
        self.r_goal = rg
        self.c_goal = cg

        #set the goal board value for node class too
        Node.goal = goal

        #initialise the positions list of the Node class
        for row in range(0,3) :
            for col in range(0,3) :
                num = Node.goal[row][col]
                Node.positions[num] = (row, col)
        #now positions list contains the indices of all numbers in the goal board




    # methods ###################################################

    def solve(self) :
        #check if problem is solvable
        #if self.isSolvable() == False :
            #print("This puzzle is not solvable. Try a different starting arrangement\n")
            #return

        #generate the tree  #uses bfs
        self.generateTree()
        #now goal node has been found

        #stack to store the nodes
        stk = deque()
        #temporary node for traversing the tree
        temp:Node = self.goal_node

        #go from goal node to root, child to parent
        #and add each node to the stack
        while temp != None :
            stk.append(temp)
            temp = temp.parent

        #print the answer path, from root to goal
        while len(stk) != 0 :
            #pop the top element
            top = stk.pop()
        
            #print the board
            print(top.board)
            print()
            print()

        #print tot states generated
        print("To reach this solution, total number of states generated is " , self.states_generated)
        print("To reach this solution, total number of states explored is " , self.states_explored)


        

    #method to check if the function is solvable
    #only for goal = [1,2,3] [4,5,6] [7,8,0]
    def isSolvable(self) -> bool:
        #solvable if start board has even no. of inversions
        #convert the 2D array to 1D
        start_arr = self.root.board.flatten()

        count = 0 #number of inversions
        #count number of inversions
        for i in range(0,9) :
            for j in range (i+1, 9) :
                #ignore 0 as its empty tile
                if (start_arr[i] > 0)  and (start_arr[j] > 0) :
                    #if (i,j) pair is inverted
                    if(start_arr[i] < start_arr[j]) :
                        count = count + 1           
        #tot 36 times

        #if count is even then solvable
        if count%2 == 0 :
            return True
        else :
            return False



    #generate the tree #bfs principle
        #self = the puzzle
    def generateTree(self) :
        #the open list
        pq = PriorityQueue()

        #add root node to queue
        pq.put((0, self.root))

        #while goal node is not found:
        while self.goal_found == False :
            #pop the front node
            #pq.get() returns tupple (child,f , child)
            tup = pq.get()
            front:Node = tup[1]
            #node with min F(x) val in the queue

            #increment the count of states explored
            self.states_explored += 1

            #generate all children of front
            up = front.moveUp()
            down = front.moveDown()
            left = front.moveLeft()
            right = front.moveRight()

            #list of children
            children = [up, down, left, right]

            #for each child
            for child in children :
                if child != None : #if child exists
                    #if the child is the goal state
                    if (child.r == self.r_goal) and (child.c == self.c_goal) :
                        #check if the board matches the goal state
                        if np.array_equal(child.board , self.goal) :
                            #goal found
                            self.goal_node = child
                            self.goal_found = True
                            return

                    #child is not goal
                    # add the child to the priority queue
                    n:int = child.f
                    pq.put((child.f , child) )  
                    
                    #increment the count of states generated
                    self.states_generated = self.states_generated + 1



#######################################################


