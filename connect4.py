import copy
import time
import numpy as np
import matplotlib.pyplot as plt



class node:
    def __init__(self,board,column,eval=None):
        self.column=column
        self.board=board
        self.children= []
        self.eval= eval

def count_nodes(node):
        """Recursively count all nodes in the tree."""
        if not node:
            return 0
        count = 1  # Count current node
        for child in node.children:
            count += count_nodes(child)
        return count

        


class connect4:
    def __init__(self):
        # Initialize game board 6x7
        self.board =[
                    [0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0]]
        
        self.current_player =  2 # 1 for human, 2 for AI
        self.winner = None  # Track winner
        self.moves = 0  # Track number of moves
        self.numberoffours = {1: 0, 2: 0} 
        self.is_full = False  # Track if board is full
        self.depth = 0
        self.algorithm = None  # To store the chosen algorithm


    def choose_algorithm(self, algorithm):
        # for GUI
        self.algorithm = algorithm
        print(f"Selected algorithm: {self.algorithm}")

    
    def choose_algorithm(self):
        #for backend
        print("Choose AI Algorithm:")
        print("1. Minimax")
        print("2. Minimax with Alpha-Beta Pruning")
        print("3. Expected Minimax")

        choice = input("Enter the number of the algorithm you want to use: ")

        if choice == "1":
            self.algorithm = self.minimax
            print("You have chosen Minimax!")
        elif choice == "2":
            self.algorithm = self.alpha_beta_pruning
            print("You have chosen Minimax with Alpha-Beta Pruning!")
        elif choice == "3":
            self.algorithm = self.expected_minimax
            print("You have chosen Expected Minimax!")
        else:
            print("Invalid choice, defaulting to Minimax.")
            self.algorithm = self.minimax
    
    def printBoard(self):
        # Print the board 
        for row in self.board:
            print(" | ".join(str(cell) if cell != 0 else '.' for cell in row))
        
    
    def dropDisc(self, board , column):
   
        if self.isValidmove(board,column):
            # Loop from the bottom row upwards to find the first available slot
            for row in reversed(board):
                if row[column] == 0:
                    row[column] = self.current_player
                    return True
        return False
    
    def isValidmove(self,board, column):
        return 0 <= column < 7 and board[0][column] == 0
    def checkForFour(self,player,board):
        if self.moves < 7:  # Minimum moves needed for a Connect 4
            return False

        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)] 
        self.numberoffours[player] = 0  

        for row in range(6):
            for col in range(7):
                if board[row][col] != player:
                    continue
 
                for dr, dc in directions:
                    count = 0
                    for i in range(4):
                        r, c = row + dr * i, col + dc * i
                        if 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
                            count += 1
                        else:
                            break
                    if count == 4:
                        print(count)
                        self.numberoffours[player] += 1

        # Check if the board is full
        self.is_full = self.moves == 42  
        return self.is_full
    

 
    def getGamestatus(self):
        if self.is_full:
            self.winner = 1 if self.numberoffours[1] > self.numberoffours[2] else 2
            loser = 3 - self.winner
            if self.numberoffours[1] == self.numberoffours[2]:
                return f"Game Over! Draw, Both players have {self.numberoffours[1]} connected fours"
            return f"Game Over! Player {self.winner} wins! Score: Player {self.winner}: {self.numberoffours[self.winner]} vs Player {loser}: {self.numberoffours[loser]}"
        else:
            return f"Current score - Player 1: {self.numberoffours[1]} fours, Player 2: {self.numberoffours[2]} fours"
            
    def move(self):
        if self.current_player == 1:
            return self.playerMove()
        else:
            return self.AIMove()
        
    def playerMove(self):
        self.printBoard()
        while True:

                column = int(input(f"Player {self.current_player}, choose a column (0-6): "))
                
                # Validate column range
                if not (0 <= column <= 6):
                    print("Please enter a number between 0 and 6.")
                    continue
                    
                # Try to drop the disc
                if self.dropDisc(self.board, column):
                    self.moves += 1 
                    self.checkForFour(self.current_player,self.board)
                    print(self.getGamestatus())
                    self.current_player = 3 - self.current_player                
                    return False
                else:
                    print("Column is full! Try another column.")

    def checkForFourAIHELPER(self, player, board):
        score = 0
        opponent = 3 - player  
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Right, Down, Down-Right, Up-Right

        player_fours = 0
        opponent_fours = 0

        for row in range(6):
            for col in range(7):
                if board[row][col] == player:  # Check player's pieces
                    for dr, dc in directions:
                        count_player = 0
                        count_opponent = 0
                        empty_spots = 0

                        # Check a line in each direction
                        for i in range(4):
                            r, c = row + dr * i, col + dc * i
                            if 0 <= r < 6 and 0 <= c < 7:
                                if board[r][c] == player:
                                    count_player += 1
                                elif board[r][c] == opponent:
                                    count_opponent += 1
                                elif board[r][c] == 0:
                                    empty_spots += 1
                            else:
                                break

                        # n7sb el score 3la 7sb 3dd el pieces w el empty spots
                        if count_player == 4:
                            player_fours += 1  # n7sb el connect 4 bta3 el player
                        elif count_opponent == 4:
                            opponent_fours += 1  # n7sb el connect 4 bta3 el opponent
                        elif count_opponent == 3 and empty_spots == 1:
                            score -= 50  # n3ml block lel opponent lw 3ndo 3 pieces wra b3d
                        elif count_player == 3 and empty_spots == 1:
                            score += 40  # nkaf2 el AI lw 3ndo 3 pieces wra b3d w mkan fady y5ls bih
                        elif count_player == 2 and empty_spots == 2:
                            score += 10  # nkaf2 el connection el nos nos
                        elif count_opponent == 2 and empty_spots == 2:
                            score -= 10  # n3a2b el opponent 3la el connection el nos nos

       
        score += (player_fours - opponent_fours) * 100  # Reward AI for more Connect 4s

        return score

    def evaluate(self,board):
        score = 0
        column_weights = [2,3,4,6,4,3,2]
        for row in range(6):
            for col in range(7):
                if board[row][col] == 2:
                    score += column_weights[col]
                    score += self.checkForFourAIHELPER(2,board)
                elif board[row][col] == 1:
                    score -= column_weights[col]
                    score -= self.checkForFourAIHELPER(1,board)
        return score
        

    
    def minimax(self, board, depth, maximizing_player, root):
        # Initialize root node with current board
        if depth == 0 or self.is_full:
            root.eval = self.evaluate(board)
            return root.eval
        
        if maximizing_player:  # AI's turn (maximizing)
            max_eval = float('-inf')
            for col in range(7):
                if self.isValidmove(board, col):
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    child_node = node(temp_board, col)
                    root.children.append(child_node)

                    eval = self.minimax(temp_board, depth - 1, False, child_node)  
                    
                    
                    child_node.eval = eval
                    
                    max_eval = max(max_eval, eval)
            return max_eval
        
        else:  # Human's turn (minimizing)
            min_eval = float('inf')
            for col in range(7):
                if self.isValidmove(board, col):
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    child_node = node(temp_board, col)
                    root.children.append(child_node)

                    eval = self.minimax(temp_board, depth - 1, True, child_node)  # Recursive call
                    
                    
                    child_node.eval = eval
                    
                    min_eval = min(min_eval, eval)
            return min_eval

    def alpha_beta_pruning(self, board, depth, alpha, beta, maximizing_player, root):
        # If the game is over or we've reached the depth limit, return the evaluation score
        if depth == 0 or self.is_full:
            root.eval = self.evaluate(board)
            return root.eval

        # Maximizing player's turn (AI)
        if maximizing_player:
            max_eval = float('-inf')
            
            for col in range(7):
                if self.isValidmove(board,col):
                    # Make the move
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    
                    
                    child_node = node(temp_board, col)
                    root.children.append(child_node)
                    
                    # Recursively call alpha_beta for the opponent
                    eval = self.alpha_beta_pruning(temp_board, depth - 1, alpha, beta, False, child_node)
                    
                    
                    child_node.eval = eval
                    
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    # Prune the branches 
                    if beta <= alpha:
                        break
            return max_eval

        # Minimizing player's turn (Opponent)
        else:
            min_eval = float('inf')
            # Try every possible move
            for col in range(7):
                if self.isValidmove(board,col):
                    # Make the move
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    
                    # Create child node and add to root before recursive call
                    child_node = node(temp_board, col)
                    root.children.append(child_node)
                    
                    # Recursively call alpha_beta for the opponent
                    eval = self.alpha_beta_pruning(temp_board, depth - 1, alpha, beta, True, child_node)
                    
                    # Update child node's eval after recursive call returns
                    child_node.eval = eval
                    
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    # Prune the branches where the value is worse than a previously found move
                    if beta <= alpha:
                        break
            return min_eval
        
    def expected_minimax(self, board, depth, maximizing_player, root):
        # If the game is over or we've reached the depth limit, return the evaluation score
        if depth == 0 or self.is_full:
            root.eval = self.evaluate(board)
            return root.eval

        if maximizing_player:
            best_value = float('-inf')
            for col in range(7):
                if self.isValidmove(board, col):
                    # Try the move for the AI (maximizing player)
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    
                    # Create child node for main column
                    child_node = node(temp_board, col)
                    root.children.append(child_node)
                    
                    # Calculate expected value considering the probabilities for the neighboring columns
                    expected_value = 0.6 * self.expected_minimax(temp_board, depth - 1, False, child_node)  # main column
                    
                    if col > 0:  # Left column exists
                        temp_board_left = copy.deepcopy(board)
                        self.dropDisc(temp_board_left, col - 1)
                        child_node_left = node(temp_board_left, col - 1)
                        root.children.append(child_node_left)
                        expected_value += 0.2 * self.expected_minimax(temp_board_left, depth - 1, False, child_node_left)
                        
                    if col < 6:  # Right column exists
                        temp_board_right = copy.deepcopy(board)
                        self.dropDisc(temp_board_right, col + 1)
                        child_node_right = node(temp_board_right, col + 1)
                        root.children.append(child_node_right)
                        expected_value += 0.2 * self.expected_minimax(temp_board_right, depth - 1, False, child_node_right)
                    
                    # Update evaluation values for all child nodes
                    child_node.eval = expected_value
                    best_value = max(best_value, expected_value)
                    
            return best_value

        else:
            # Minimizing player's turn (opponent)
            best_value = float('inf')
            for col in range(7):
                if self.isValidmove(board, col):
                    # Try the move for the opponent (minimizing player)
                    temp_board = copy.deepcopy(board)
                    self.dropDisc(temp_board, col)
                    
                    # Create child node for main column
                    child_node = node(temp_board, col)
                    root.children.append(child_node)
                    
                    # Calculate expected value considering the probabilities for the neighboring columns
                    expected_value = 0.6 * self.expected_minimax(temp_board, depth - 1, True, child_node)  # main column
                    
                    if col > 0:  # Left column exists
                        temp_board_left = copy.deepcopy(board)
                        self.dropDisc(temp_board_left, col - 1)
                        child_node_left = node(temp_board_left, col - 1)
                        root.children.append(child_node_left)
                        expected_value += 0.2 * self.expected_minimax(temp_board_left, depth - 1, True, child_node_left)
                        
                    if col < 6:  # Right column exists
                        temp_board_right = copy.deepcopy(board)
                        self.dropDisc(temp_board_right, col + 1)
                        child_node_right = node(temp_board_right, col + 1)
                        root.children.append(child_node_right)
                        expected_value += 0.2 * self.expected_minimax(temp_board_right, depth - 1, True, child_node_right)
                    
                    # Update evaluation values for all child nodes
                    child_node.eval = expected_value
                    best_value = min(best_value, expected_value)
                    
            return best_value

    def print_tree(self, node, level=0, prefix="Root: "):
        """Print the game tree in a readable format"""
        if node is None:
            return
            
        # Print current node
        indent = "  " * level
        if node.column is not None:
            print(f"{indent}{prefix}Column {node.column}, Eval: {node.eval}")
        else:
            print(f"{indent}{prefix}Eval: {node.eval}")
            
        # Print all children
        for i, child in enumerate(node.children):
            self.print_tree(child, level + 1, f"Child {i}: ")

    def AIMove(self):
        self.printBoard()
        print(f"AI (Player {self.current_player}) is making a move...")

        best_move = None
        best_value = float('-inf')
        best_root = None
        
        if self.moves == 0:
            best_move = 3
        # Try all columns and pick the one that maximizes the AI's score using Minimax
        else: 
            for col in range(7):
                if self.isValidmove(self.board,col):
                    temp_board = copy.deepcopy(self.board)
                    self.dropDisc(temp_board, col)  # Drop AI's disc in the column
                    root = node(temp_board,column=None)
                    if self.algorithm == self.minimax or self.algorithm == self.expected_minimax:
                        move_value = self.algorithm(temp_board, self.depth, False, root)  # Recursively evaluate
                    else:
                        move_value = self.algorithm(temp_board, self.depth, float('-inf'), float('inf'), False,root)
                    if move_value > best_value:  # Update best move if this one is better
                        best_value = move_value
                        best_move = col
                        best_root = root

        # Make the best move by dropping the disc in the selected column
        self.dropDisc(self.board, best_move)
        self.moves += 1
        self.checkForFour(self.current_player, self.board)  # Check for a win after the move
        print(self.getGamestatus())  # Print game status
        
        # Print the game tree for this move
        print("\nGame tree for this move:")
        #self.print_tree(best_root)
        print()
        
        self.current_player = 3 - self.current_player  # Switch players (1 <-> 2)
        
        return False  # Since game is still ongoing after the move, return False

   
    
    def generate_comparison_report(self):
            
        # Create arrays to store results
        depths = np.array(range(1, 5))
        minimax_times = np.zeros(4)
        minimax_nodes = np.zeros(4)
        alphabeta_times = np.zeros(4) 
        alphabeta_nodes = np.zeros(4)
        
        # Collect data for each depth
        for i, depth in enumerate(depths):
            self.depth = depth
            
            # Test minimax
            root = node(copy.deepcopy(self.board), None)
            start_time = time.time()
            _ = self.minimax(self.board, depth, True, root)
            minimax_times[i] = time.time() - start_time
            minimax_nodes[i] = count_nodes(root)
            
            # Test alpha-beta
            root = node(copy.deepcopy(self.board), None)
            start_time = time.time()
            _ = self.alpha_beta_pruning(self.board, depth, float('-inf'), float('inf'), True, root)
            alphabeta_times[i] = time.time() - start_time
            alphabeta_nodes[i] = count_nodes(root)

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Plot time comparison
        ax1.plot(depths, minimax_times, 'b-o', label='Minimax')
        ax1.plot(depths, alphabeta_times, 'r-o', label='Alpha-Beta')
        ax1.set_xlabel('Depth (K)')
        ax1.set_ylabel('Time (seconds)')
        ax1.set_title('Time Comparison')
        ax1.legend()
        ax1.grid(True)
        
        # Plot nodes comparison
        ax2.plot(depths, minimax_nodes, 'b-o', label='Minimax')
        ax2.plot(depths, alphabeta_nodes, 'r-o', label='Alpha-Beta')
        ax2.set_xlabel('Depth (K)')
        ax2.set_ylabel('Nodes Expanded')
        ax2.set_title('Nodes Expanded Comparison')
        ax2.legend()
        ax2.grid(True)
        
        plt.suptitle('Algorithm Performance Comparison')
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('algorithm_comparison.png')
        plt.close()
        
        print("\nComparison report has been generated and saved as 'algorithm_comparison.png'")    
        
    def start_game(self):
        self.choose_algorithm()
        print("Welcome to Connect 4!")
        print("Player 1 is Human, Player 2 is AI")
        print("Enter column number (0-6) to drop your disc")
        
        while not self.is_full:
            if self.move():  # if move returns True, game should end
                break
                
            if self.winner:
                print(f"Player {self.winner} wins!")
                break

        # Print the final game status
        self.printBoard()
        print(self.getGamestatus())
    
def main():
    game = connect4()
    #game.start_game()
    game.generate_comparison_report()
   # Initialize the game
    #connect4_instance = connect4()

    # Initialize the root node
   # root_node = node(board=connect4_instance.board, column=None, eval=None)

    # Run the expected minimax algorithm
   # connect4_instance.alpha_beta_pruning(connect4_instance.board, depth=2, alpha=float('-inf'), beta=float('inf'), maximizing_player=True, root=root_node)

    # Print the tree after running the algorithm
   # print_tree(root_node)


if __name__ == "__main__":
    main()
