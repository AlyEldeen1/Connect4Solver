import matplotlib.pyplot as plt
import networkx as nx
from connect4 import connect4, node
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def visualize_game_tree(root_node, max_depth=4):
   
    # Create the main window
    window = tk.Tk()
    window.title("Game Tree Visualization")
    window.geometry("1200x800")
    
    G = nx.Graph()
    pos = {}
    labels = {}
    
    def add_nodes_edges(node, x, y, depth=0, parent_id=None, node_id=0):
        if depth > max_depth or node is None:
            return node_id + 1
        
        # Add node
        G.add_node(node_id)
        pos[node_id] = (x, -y)
        
        # Create label
        if node.column is not None:
            if node.eval is not None:
                labels[node_id] = f"Col:{node.column}\nEval:{node.eval:.2f}"
            else:
                labels[node_id] = f"Col:{node.column}\nEval:None"
        else:
            if node.eval is not None:
                labels[node_id] = f"Root\nEval:{node.eval:.2f}"
            else:
                labels[node_id] = f"Root\nEval:None"
            
        # Add edge to parent
        if parent_id is not None:
            G.add_edge(parent_id, node_id)
            
        # Process children
        next_id = node_id + 1
        num_children = len(node.children)
        if num_children > 0:
            spacing = 1.0 / (num_children + 1)
            for i, child in enumerate(node.children):
                child_x = x - 0.5 + spacing * (i + 1)
                next_id = add_nodes_edges(child, child_x, y + 1, depth + 1, node_id, next_id)
                
        return next_id

    # Build the graph
    add_nodes_edges(root_node, 0.5, 0)
    
    # Create the visualization
    fig = plt.figure(figsize=(15, 10))
    nx.draw(G, pos, labels=labels, with_labels=True, 
            node_color='lightblue', node_size=2500, 
            font_size=8, font_weight='bold')
    plt.title("Game Tree Visualization")
    plt.axis('off')
    
    # Embed the plot in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Add a quit button
    quit_button = tk.Button(window, text="Close", command=window.quit)
    quit_button.pack(side=tk.BOTTOM)
    
    # Start the GUI event loop
    window.mainloop()

def main():
    print("Choose algorithm to visualize:")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")
    print("3. Expected Minimax")
    
    choice = input("Enter choice (1-3): ")
    
    game = connect4()
    game.depth = 2
    root = node(game.board, None)
    
    if choice == "1":
        print("\nVisualizing Minimax Algorithm")
        game.algorithm = game.minimax
        game.minimax(game.board, game.depth, True, root)
    elif choice == "2":
        print("\nVisualizing Alpha-Beta Pruning Algorithm") 
        game.algorithm = game.alpha_beta_pruning
        game.alpha_beta_pruning(game.board, game.depth, float('-inf'), float('inf'), True, root)
    elif choice == "3":
        print("\nVisualizing Expected Minimax Algorithm")
        game.algorithm = game.expected_minimax
        game.expected_minimax(game.board, game.depth, True, root)
    else:
        print("Invalid choice. Defaulting to Minimax.")
        game.algorithm = game.minimax
        game.minimax(game.board, game.depth, True, root)
        
    # Visualize the tree
    visualize_game_tree(root)
    
    # Print node count
    from connect4 import count_nodes
    total_nodes = count_nodes(root)
    print(f"\nTotal number of nodes in tree: {total_nodes}")

if __name__ == "__main__":
    main()
