# Rock Paper Scissors Game

A simple Rock–Paper–Scissors game with a **Tkinter** GUI (MVC-style structure: UI + Logic + Controller).

## Features
- Choose: Rock / Paper / Scissors
- Computer picks randomly
- Shows result message (win/lose/tie) and computer choice
- "Play Again" resets buttons and message
- "Exit" closes the app

![First page](https://i.ibb.co/V0Hq6FvM/Screenshot-2026-02-10-213901.png)
![Example of result](https://i.ibb.co/BHfVdBLM/Screenshot-2026-02-10-214006.png)

## Requirements
- Python 3.x
- Tkinter (usually included with Python on Windows/macOS; on some Linux distros you may need to install it)

## Project Structure
```
RockPaperScissors/
├─ main.py
├─ game/
│  └─ logic.py
├─ UI/
│  └─ window.py
└─ controler/
   └─ gamecontroller.py
```
## How it works
- UI buttons call controller methods.
- Controller calls logic.play(user_choice) to get the result string.
- Controller updates the message label and disables other choice buttons until "Play Again" is pressed.

## How to run
1. Clone/download the project.
2. Run:

```bash
cd RockPaperScissors
python main.py
```