class GameController :

    def __init__(self , logic , window):

        self.logic = logic
        self.window = window

        self.window.rock_btn_set_command(command = lambda : self.play_game("rock"))
        self.window.paper_btn_set_command(command = lambda : self.play_game("paper"))
        self.window.scissors_btn_set_command(command =lambda : self.play_game("scissors"))
        self.window.play_again_btn_set_command(command = self.play_again)
        self.window.exit_btn_set_command(command = self.exit_game)

    

    def play_game (self , user_option):

         self.window.disable_btns(user_option)
         result = self.logic.play(user_option)
         self.window.set_message(result)
        

    def play_again(self) :

        self.window.enable_btns()
        self.window.set_message(message = "Enter Your choise , Plesse.")

    def exit_game(self) :
        self.window.root.destroy()


        