import tkinter as tk
from game.logic import RockPaperScissors
from UI.window import MainWindow
from controler.gamecontroller import GameController


def main() :
    root = tk.Tk() 
    root.configure(bg="lightpink") 
    window = MainWindow(root)
    logic = RockPaperScissors()
    controller = GameController(logic=logic, window=window)
    root.mainloop()

if __name__ == "__main__" :

    main()
