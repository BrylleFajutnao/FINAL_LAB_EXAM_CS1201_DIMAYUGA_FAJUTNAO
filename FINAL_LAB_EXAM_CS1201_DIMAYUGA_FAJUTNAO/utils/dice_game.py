import os
import random
from datetime import datetime

class DiceGame:
    def load_scores():
        pass

    def save_scores():
        pass

    def play_game(self):
        
        pass

    def show_topscores(self):
        highest_score = self.load_highest_score()
        highest_score_date = self.load_highest_score_date()
        if highest_score is not None:
            print(f"Highest Score: {highest_score} (Achieved on: {highest_score_date})")
        else:
            print("No highest score recorded yet.")
        pass

    def log_out(self):
        print("Exiting the game.")
        return
        pass

    def menu(self):
        while True:
            print("Random Dice Game")
            print("Welcome {self.user}")
            print("1. start")
            print("2. top scores")
            print("3. logout")

            choice=int(input("Enter your choice: "))

            try:
                if choice == 1:
                    self.play_game()
                elif choice ==2:
                    self.show_topscores()
                elif choice == 3:
                    self.log_out()
                else:
                    print("enter a number between 1-3")
            except ValueError:
                print("please enter a number")
        pass