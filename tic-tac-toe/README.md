# Tic Tac Toe - MinMax
An interactive Tic Tac Toe game with a Streamlit GUI where you play against an AI opponent.

## Features

-  **AI** using Minimax algorithm
-  **Three difficulty levels**: Easy, Medium, Hard
-  **Score tracking system**: Records wins, losses, and draws
-  **GUI** built with Streamlit
-  Game **restart** functionality
-  **AI thinking animation** for better user experience

<img src="https://i.ibb.co/5gRgyb74/Screenshot-2026-02-15-144912.png" alt="GUI Preview" width="400">

## Project Structure
```
tictactoe-ai/
├── app.py              
├── game.py             
├── README.md           
└── requirements.txt 
```
## Algorithms
Minimax Algorithm 
In Hard mode, the AI uses the Minimax algorithm, which explores all possible game states and selects the optimal move, making it unbeatable.
Difficulty Levels:
- Easy: Completely random moves
- Medium: Mix of random (50%) and optimal moves (50%)
- Hard: Uses Minimax algorithm (unbeatable)

## Requirements
- Python 3.x
- Packages:
  - streamlit

## How To Run 
1. Download project or clone the repository
2. cd to tic_tac_to folder
3. Install dependencies
``` bash
pip install streamlit
```
4. To Run GUI mode
``` bash
streamlit run app.py
```
The app will open in your browser 

5. To Run Console Mode :
``` bash
python game.py
```

## How to Play
1. Select difficulty level from the dropdown menu at the top
2. Click on an empty cell to place your X
3. AI automatically places its O
4. Win condition: Get three marks in a row (horizontal, vertical, or diagonal)
5. Restart the game using the 🔄 Restart Game button
