import random


class RockPaperScissors :

    def __init__(self):
        self.choices = ['rock' , 'paper' ,'scissors']


    def get_computer_choice (self) :

        return random.choice(self.choices) 

    def decide_winner (self , user_choice , computer_choice):

        win_combinations = [('rock' , 'scissors') , ('scissors' , 'paper'),('paper' , 'rock')]
    
        if user_choice == computer_choice :
            return "It's a Tie.Would You Like To Playe again? Enter the key!"

        elif (user_choice , computer_choice ) in win_combinations :
            return f"Congratulation! You Won! Computer Choice :{computer_choice}.Would You Like To Playe again? Enter the key!"
        
        else :
            return f"Oh no! Computer Won. Computer choice : {computer_choice}.Would You Like To Playe again? Enter the key!"

   
    def play(self, user_choice):
      computer_choice = self.get_computer_choice()
      return self.decide_winner(user_choice, computer_choice)
    