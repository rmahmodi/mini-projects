import tkinter as tk

class MainWindow :

    def __init__(self , root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x250")

        

        self.main_frame = tk.Frame(self.root , bg = "lightpink")
        self.message_label = tk.Label(self.main_frame , 
                                      text="Enter Your choise , Plesse." ,
                                        bg="lightpink", font=("Segoe UI Emoji" , 20))
        self.btn_rock = tk.Button(self.main_frame , text='Rock')
        self.btn_paper = tk.Button(self.main_frame , text ="Paper")
        self.btn_scissors = tk.Button(self.main_frame , text="Scissors")
        self.btn_play_again = tk.Button(self.main_frame , text="Play Again")
        self.btn_exit = tk.Button(self.main_frame , text="Exit")

        self.rps_buttons = [self.btn_rock , self.btn_paper , self.btn_scissors]

        self.main_frame.pack()
        self.message_label.grid(row=0, column=0, columnspan=3, pady=15)
        self.btn_rock.grid(row=1, column=0, padx=5, pady=5)
        self.btn_paper.grid(row=1, column=1, padx=5, pady=5)
        self.btn_scissors.grid(row=1, column=2, padx=5, pady=5)
        self.btn_play_again.grid(row=2, column=0, columnspan=3, sticky="ew", padx=5, pady=10)
        self.btn_exit.grid(row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=10)

    def set_message(self , message) :
        self.message_label.config(text = message)

    def rock_btn_set_command (self , command) :
        self.btn_rock.config(command=command)

    def paper_btn_set_command (self , command) :
        self.btn_paper.config(command=command)

    def scissors_btn_set_command (self , command) :
        self.btn_scissors.config(command=command)

    def play_again_btn_set_command (self , command) :
        self.btn_play_again.config(command=command)

    def exit_btn_set_command (self , command) :
        self.btn_exit.config(command=command)

    def disable_btns (self , option) :

        for btn in self.rps_buttons:
         if btn["text"].lower() != option:
             btn.config(state="disabled")
    
    def enable_btns(self) :
        
        for btn in self.rps_buttons:
          btn.config(state="normal")



        
        
        
        
        
