//dfs solving

import java.util.Arrays;
import java.util.Stack;
import java.util.HashMap;

//node of a tree
class Node{ 
    //hashmap containing all the Nodes in the tree
    static HashMap<int[][], Node> nodes = new HashMap<>();
    // node.board : node
    //static ---> only 1 global copy of the class

    //value of the board
    int[][] board = new int[3][3]; 

    //the child nodes
    Node up;    
    Node down;   
    Node left;
    Node right;

    //parent node
    Node parent; 
    
    //index of the empty tile
    int r, c;

    //what move of parent created this node
    String move; // up down left right

    //constructor
    Node(int[][] arr){
        this.board = arr;
        right=null;
        left=null;
        up=null;
        down=null;
    }

    //methods
    //create child nodes
    public Node move_up(){
        //if empty tile cant be moved up
        if(this.r == 0){
            return null;
        }

        int [][] child_board = this.clone_array() ;

        //create the child node
        Node child = new Node(child_board);
        //now child node's board is exact copy of the parent board

        //move the empty tile up in the child board
        // (r,c) = 0
        // exchange (r,c) and (r-1, c)
        child.board[r][c] = child.board[r-1][c] ;
        child.board[r-1][c] = 0;

        if( nodes.containsKey(child.board) ){
            //this arrangement of the board already exists in the tree
            //so dont add this child node to the tree
            return null;
        }else{
            //add the board to the list of nodes
            nodes.put(child.board, child) ;

        }

        //updating the fields of the child node
        child.parent = this;
        child.r = r-1;
        child.c = c;
        child.move = "up";

        //return the child node
        return child;
    }

    public Node move_down(){
        //if empty tile cant be moved down
        if(this.r == 2){
            return null;
        }

        int [][] child_board = this.clone_array() ;

        //create the child node
        Node child = new Node(child_board);
        //now child node's board is exact copy of the parent board

        //move the empty tile down in the child board
        // (r,c) = 0
        // exchange (r,c) and (r+1, c)
        child.board[r][c] = child.board[r+1][c] ;
        child.board[r+1][c] = 0;

        if( nodes.containsKey(child.board) ){
            //this arrangement of the board already exists in the tree
            //so dont add this child node to the tree
            return null;
        }else{
            //add the board to the list of nodes
            nodes.put(child.board, child) ;

        }

        //updating the fields of the child node
        child.parent = this;
        child.r = r+1;
        child.c = c;
        child.move = "down";

        //return the child node
        return child;
    }


    public Node move_left(){
        //if empty tile cant be moved left
        if(this.c == 0){
            return null;
        }

        int [][] child_board = this.clone_array() ;

        //create the child node
        Node child = new Node(child_board);
        //now child node's board is exact copy of the parent board

        //move the empty tile left in the child board
        // (r,c) = 0
        // exchange (r,c) and (r, c-1)
        child.board[r][c] = child.board[r][c-1] ;
        child.board[r][c-1] = 0;

        if( nodes.containsKey(child.board) ){
            //this arrangement of the board already exists in the tree
            //so dont add this child node to the tree
            return null;
        }else{
            //add the board to the list of nodes
            nodes.put(child.board, child) ;

        }

        //updating the fields of the child node
        child.parent = this;
        child.r = r;
        child.c = c-1;
        child.move = "left";

        //return the child node
        return child;
    }


    public Node move_right(){
        //if empty tile cant be moved right
        if(this.c == 2){
            return null;
        }

        int [][] child_board = this.clone_array() ;

        //create the child node
        Node child = new Node(child_board);
        //now child node's board is exact copy of the parent board

        //move the empty tile right in the child board
        // (r,c) = 0
        // exchange (r,c) and (r, c+1)
        child.board[r][c] = child.board[r][c+1] ;
        child.board[r][c+1] = 0;

        if( nodes.containsKey(child.board) ){
            //this arrangement of the board already exists in the tree
            //so dont add this child node to the tree
            return null;
        }else{
            //add the board to the list of nodes
            nodes.put(child.board, child) ;

        }

        //updating the fields of the child node
        child.parent = this;
        child.r = r;
        child.c = c+1;
        child.move = "right";

        //return the child node
        return child;
    }


    //function to clone the board of parent node
    public int[][] clone_array(){
        if (this.board == null) {
            return null;
        }
 
        int[][] copy = new int[this.board.length][];
        for (int i = 0; i < this.board.length; i++) {
            copy[i] = this.board[i].clone();
        }
 
        return copy;
    }
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





public class eight_puzzle{
    //start state is the root node
    //goal array is global variable
    static int[][] goal =  {{1,2,3}, {4,5,6}, {7,8,0}} ;

    //index of empty tile in goal state
    static int r_goal =2;
    static int c_goal = 2;

    //global reference to the goal node
    static Node goal_node;
    //whether goal node has been generated or not
    static Boolean goalFound = false; 


    public static void main(String[] args) {
        int[][] start = {{1,2,3}, {0,4,6}, {7,5,8}};
        
        //index of the empty tile in start
        int r = 1;
        int c = 0;

        //check if the puzzle is solvable

        solve(start, r, c);
    }

    
    public static void solve(int[][] start, int r, int c){
        //check if the problem can be solved
        if ( ! isSolvable(start) ){
            System.out.println("The problem cannot be solved, try a different starting arrangement.\n");
            return;
        }
        //working fine till here

        //creating the root node of the tree
        Node root = new Node(start);
        root.parent = null;
        root.r = r;
        root.c = c;
        root.move = "initial";

        //add root node to hashmap nodes
        Node.nodes.put(start, root) ;
        //access the hashmap "nodes" as Node.nodes as 
        //the hashmap belongs to Node class
        //working fine till here

        //generate the tree
        generate_tree(root) ;
        //never reaching here, infinite recursion??
        System.out.println("tree generated.");
        System.out.println("goal found is " + goalFound + "\n");
        //now the goal node is found

        Stack<Node> answer = new Stack<>();
        //go from goal node to root node, and add each node to the stack
        Node temp = goal_node ; //node for traversal
        while(temp != null){
            answer.push(temp) ;
            temp = temp.parent;
        }

        //now print each element of the stack from top to bottom
        while( ! answer.isEmpty()){
            Node top = answer.pop() ;

            int[][] arr = top.board;

            //print the board
            for(int i=0;  i<arr.length ; i++){
                System.out.println( Arrays.toString(arr[i]) );
            } 
        }

    }


    public static Boolean isSolvable(int[][] start){
        int[] start_1d = convert_2D_to_1D(start);   //9 times

        int count = 0;
        //count number of inversions
        for(int i=0; i<9; i++){
            for(int j=i+1; j<9; j++){
                //ignore 0
                if(start_1d[i] > 0  && start_1d[j] > 0){
                    //if (i,j) pair is inverted
                    if(start_1d[i] < start_1d[j]){
                        count++ ;
                    }
                }
            }
        }
        //tot 36 times

        // return true if count is even
        if(count%2 == 0){
            return true;
        }
        // else
        return false;
    }
    //tot 45 times //O(1) time complexity


    //function to convert the 2D matrix into a 1D array
    public static int[] convert_2D_to_1D(int[][] mat){
        //matrix will be a 3x3 array
        //so tot 9 elements
        int[] arr = new int[9];

        //array index
        int ind = 0;

        //copying matrix elements to 1D array
        for(int i=0;  i<3 ; i++){
            for(int j=0; j<3 ; j++){
                arr[ind] = mat[i][j] ;
                ind++ ;
            }
        }

        return arr;
    }
    ///TC = O(1)   //9 times





    //problem here /////////////////////////////////////////////////////////////////
    //function exiting before goal node is found?????????????????????????????????????????
    //generate the tree and return the goal node
    public static void  generate_tree(Node n){
        if(goalFound){return;}
        //goal node has already been generated, so no need to create anymore nodes 

        if(n==null){return ;}

        //printMatrix(n.board);
        //System.out.println();

        //if empty tile index of node n and goal match
        //then check if node n is the goal node
        if(n.r == r_goal && n.c==c_goal){
            if (Arrays.deepEquals(goal, n.board)){
                //node n is the goal node
                goal_node = n;
                goalFound = true;
                return ;
            }
        }

        //n is not the goal node
        //generate its child nodes
        n.up = n.move_up() ;
        n.down = n.move_down();
        n.left = n.move_left() ;
        n.right = n.move_right() ;

        if(n.move == "up"){
            //recursive calls
            //to generate the child nodes of the child nodes
            generate_tree(n.up);    
            generate_tree(n.left);
            generate_tree(n.right);
        }
        else if(n.move == "down"){
            //recursive calls
            //to generate the child nodes of the child nodes
            generate_tree(n.down);    
            generate_tree(n.left);
            generate_tree(n.right);
        }
        else if(n.move == "left"){
            //recursive calls
            //to generate the child nodes of the child nodes
            generate_tree(n.down);    
            generate_tree(n.left);
            generate_tree(n.up);
        }
        else if(n.move == "right"){
            //recursive calls
            //to generate the child nodes of the child nodes
            generate_tree(n.down);    
            generate_tree(n.up);
            generate_tree(n.right);
        }
        else if(n.move=="initial"){
            //this is the start state
            //recursive calls
            //to generate the child nodes of the child nodes
            generate_tree(n.up); 
            generate_tree(n.down);   
            generate_tree(n.left);
            generate_tree(n.right);
        }

        return;
        
    }


    //function to print a 2D matrix
    public static void printMatrix( int[][] arr) {
        for(int i=0;  i<arr.length ; i++){
            System.out.println( Arrays.toString(arr[i]) );
        } 
    }


}