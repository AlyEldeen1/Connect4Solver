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
