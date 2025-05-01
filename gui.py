import tkinter as tk
from tkinter import messagebox
from connect4 import connect4

class Connect4GUI:
    def __init__(self, root, connect4_backend):
        self.root = root
        self.connect4 = connect4_backend  # Connect to the backend
        self.buttons = []  # List to store button references for each column
        self.algorithm_choice = None  # Store the selected algorithm
        self.game_running = False  # Flag to track game state

        # Configure root window
        self.root.configure(bg='#2C3E50')  # Dark blue background
        self.root.title("Connect 4")
        
        # Create main frame with padding
        self.main_frame = tk.Frame(root, bg='#2C3E50', padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Initialize the GUI components
        self.create_buttons()
        self.create_algorithm_selector()

    def create_buttons(self):
        """Create the board as a 6x7 grid of buttons."""
        board_frame = tk.Frame(self.main_frame, bg='#34495E', padx=10, pady=10)
        board_frame.pack()

        for row in range(6):
            button_row = []
            for col in range(7):
                # Create a canvas instead of a button to draw circles
                canvas = tk.Canvas(board_frame,
                                 width=60,
                                 height=60,
                                 bg='#ECF0F1',
                                 highlightthickness=1,
                                 highlightbackground='#34495E')
                canvas.grid(row=row, column=col, padx=2, pady=2)
                # Draw empty circle
                canvas.create_oval(10, 10, 50, 50, fill='#ECF0F1', outline='#BDC3C7')
                canvas.bind('<Button-1>', lambda e, col=col: self.on_column_click(col))
                button_row.append(canvas)
            self.buttons.append(button_row)

    def create_algorithm_selector(self):
        """Create a dropdown for selecting the algorithm."""
        control_frame = tk.Frame(self.main_frame, bg='#2C3E50', pady=15)
        control_frame.pack()

        self.algorithm_var = tk.StringVar(self.root)
        self.algorithm_var.set("Minimax")  # Default choice
        
        algorithms = ["Minimax", "Alpha-Beta Pruning", "Expected Minimax"]
        
        # Style the dropdown
        algorithm_menu = tk.OptionMenu(control_frame, self.algorithm_var, *algorithms)
        algorithm_menu.config(width=20, 
                            font=('Arial', 10),
                            bg='#3498DB',
                            activebackground='#2980B9',
                            fg='white')
        algorithm_menu["menu"].config(bg='#3498DB', fg='white')
        algorithm_menu.pack(pady=5)

        # Style the start button
        start_button = tk.Button(control_frame,
                               text="Start Game",
                               command=self.start_game,
                               font=('Arial', 12, 'bold'),
                               bg='#27AE60',
                               fg='white',
                               activebackground='#219A52',
                               width=15,
                               height=1,
                               relief="raised")
        start_button.pack(pady=5)

    def start_game(self):
        """Start the game and control the flow in the GUI."""
        if self.game_running:
            return
        
        self.algorithm_choice = self.algorithm_var.get()
        
        # Set the algorithm in backend based on selection
        if self.algorithm_choice == "Minimax":
            self.connect4.algorithm = self.connect4.minimax
        elif self.algorithm_choice == "Alpha-Beta Pruning":
            self.connect4.algorithm = self.connect4.alpha_beta_pruning
        else:
            self.connect4.algorithm = self.connect4.expected_minimax

        # Disable controls during game
        for child in self.main_frame.winfo_children():
            if isinstance(child.winfo_children()[0], tk.OptionMenu):
                child.winfo_children()[0].config(state="disabled")
            if isinstance(child.winfo_children()[-1], tk.Button):
                child.winfo_children()[-1].config(state="disabled")

        self.game_running = True
        self.update_board()
        self.game_loop()

    def game_loop(self):
        """Loop through the game and control the player turns."""
        if self.connect4.winner or self.connect4.is_full:
            self.end_game()
            return
        
        if self.connect4.current_player == 2:  # AI's turn
            self.root.after(500, self.ai_move)
        else:  # Human player's turn
            self.root.after(100, self.check_game_status)

    def ai_move(self):
        """Let the AI make its move and update the board."""
        if not self.game_running:
            return
        
        self.connect4.AIMove()
        self.update_board()
        self.check_game_status()

    def on_column_click(self, col):
        """Handle the button press for choosing the column."""
        if not self.game_running or self.connect4.current_player != 1:
            return

        if self.connect4.dropDisc(self.connect4.board, col):
            self.connect4.moves += 1
            self.connect4.checkForFour(self.connect4.current_player, self.connect4.board)
            self.connect4.current_player = 3 - self.connect4.current_player
            self.update_board()
            self.check_game_status()
            self.game_loop()

    def update_board(self):
        """Update the visual state of the board after a move."""
        for row in range(6):
            for col in range(7):
                canvas = self.buttons[row][col]
                canvas.delete("all")  # Clear previous circle
                if self.connect4.board[row][col] == 1:
                    canvas.create_oval(10, 10, 50, 50, fill='#E74C3C', outline='#C0392B')
                elif self.connect4.board[row][col] == 2:
                    canvas.create_oval(10, 10, 50, 50, fill='#F1C40F', outline='#D4AC0D')
                else:
                    canvas.create_oval(10, 10, 50, 50, fill='#ECF0F1', outline='#BDC3C7')

    def show_popup(self, message):
        """Show a popup message with game status."""
        messagebox.showinfo("Game Over", message)

    def check_game_status(self):
        """Check if the game is over."""
        if self.connect4.winner:
            self.end_game(f"Player {self.connect4.winner} wins!")
        elif self.connect4.is_full:
            self.end_game("It's a draw!")

    def end_game(self, message="Game Over"):
        """End the game and show a popup."""
        self.show_popup(message)
        self.game_running = False
        
        # Re-enable controls
        for child in self.main_frame.winfo_children():
            if isinstance(child.winfo_children()[0], tk.OptionMenu):
                child.winfo_children()[0].config(state="normal")
            if isinstance(child.winfo_children()[-1], tk.Button):
                child.winfo_children()[-1].config(state="normal")

def main():
    root = tk.Tk()
    root.title("Connect 4")
    
    game_backend = connect4()
    game_backend.depth = 3
    gui = Connect4GUI(root, game_backend)
    
    root.mainloop()

if __name__ == "__main__":
    main()
