# Connect 4 Game with AI

This project is a complete implementation of the Connect 4 game, featuring both a backend (game logic and AI) and a frontend (user interface) for an interactive user experience. The backend consists of the game logic, AI algorithms, and game state management, while the frontend provides a graphical user interface to play the game.

## Features

### Backend:
- **AI Opponent**: Choose between Minimax, Alpha-Beta Pruning, and Expected Minimax algorithms.
- **Game State Management**: Handles the state of the board, player turns, and checks for wins or draws.
- **Tree Visualization**: Displays the decision tree for AI moves.
- **Heuristic Evaluation**: AI evaluates moves based on custom heuristic evaluation functions.

### Frontend:
- **Graphical Interface**: A simple web-based interface to interact with the game.
- **Real-time Updates**: The board and game status update in real-time.
- **Move Input**: Players can click on columns to make their moves.
- **AI vs Human Mode**: Play against an AI opponent with different algorithms or with another human.

## Technologies Used

- **Backend**: Python, Flask (for API and server-side logic), NumPy (for handling game logic and board evaluation)
- **Frontend**: HTML, CSS, JavaScript, React.js (for dynamic rendering of the game state)
- **AI Algorithms**: Minimax, Alpha-Beta Pruning, Expected Minimax
- **Visualization**: Graphviz for AI tree visualization
- **Dependencies**:
  - Flask
  - NumPy
  - React
  - Axios (for API calls)

## Installation

### Backend Setup

1. Clone the repository:


git clone https://github.com/yourusername/connect4-ai.git
cd connect4-ai
Install the necessary Python dependencies:

bash
نسخ
تحرير
pip install -r backend/requirements.txt
Run the Flask server:

bash
نسخ
تحرير
cd backend
python app.py
The backend should now be running at http://localhost:5000.

Frontend Setup
Navigate to the frontend directory:

bash
نسخ
تحرير
cd frontend
Install the necessary JavaScript dependencies:

bash
نسخ
تحرير
npm install
Start the React development server:

bash
نسخ
تحرير
npm start
The frontend should now be running at http://localhost:3000.

Usage
Once both the backend and frontend are running, open your browser and go to http://localhost:3000 to play the game.

How to Play:
Human vs AI: Choose to play against the AI by selecting one of the available algorithms (Minimax, Alpha-Beta Pruning, or Expected Minimax). The AI will make its move automatically.

Human vs Human: Play with a friend in two-player mode by taking turns to select columns to drop pieces.

AI Visualization: The backend provides a visualization of the decision tree for AI moves, which can be toggled on/off in the game settings.

Example API Requests (Backend)
Starting a new game:
bash
نسخ
تحرير
POST /api/start_game
Making a move:
bash
نسخ
تحرير
POST /api/move
{
  "player": 1,
  "column": 3
}
Get current game state:
bash
نسخ
تحرير
GET /api/game_state
AI Algorithm Choices:
Minimax: A basic AI algorithm that evaluates all possible moves and selects the best one based on a simple evaluation function.

Alpha-Beta Pruning: An optimized version of Minimax that prunes branches of the game tree, making it more efficient.

Expected Minimax: A probabilistic version of Minimax that takes into account expected outcomes rather than strict evaluation.

Visualizing the AI's Decision Tree:
The game provides a graphical tree of AI decisions, allowing players to see how the AI evaluates its moves at a certain depth.

Example of Game Interaction
Start a New Game
The game will begin with the user selecting either to play with a friend or against the AI. The game board is displayed in the frontend interface, and the user can click on columns to drop their pieces.

Gameplay Flow
Human's Turn: The player selects a column to drop their piece.

AI's Turn: If playing against the AI, the backend calculates the next move using the selected algorithm (e.g., Minimax) and updates the board.

Game Over: The game will automatically detect and announce the winner or a draw.

Project Structure
backend/: Contains the game logic, AI algorithms, and Flask API.

app.py: The main Flask server that serves the API and handles game logic.

game.py: Contains the game logic, including the Connect 4 board management and AI algorithms.

ai.py: Implements the AI algorithms such as Minimax, Alpha-Beta Pruning, and Expected Minimax.

frontend/: Contains the React.js app for the user interface.

src/: Contains React components for rendering the board and handling user interactions.

public/: Contains static assets (e.g., images, icons).

index.js: The entry point for the React application.

Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome, especially improvements to the AI algorithms or the game interface.

License
This project is open-source and available under the MIT License.

Enjoy playing Connect 4 with AI and testing out different strategies!

python
نسخ
تحرير

### Notes:
- You should replace the placeholder URLs with the actual repository link for your project.
- Ensure that the file structure matches the paths mentioned in the `README.md`.
- This template assumes a full-stack setup with Flask as the backend and React.js for the frontend. If you're using a different framework for either, adjust the instructions accordingly.

Let me know if you'd like further tweaks or additional information!
