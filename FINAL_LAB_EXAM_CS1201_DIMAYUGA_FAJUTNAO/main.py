from utils.dice_game import DiceGame
from utils.user import User
from utils.usermanager import UserManager
from utils.score import Score

def main():

    while True:
        while True:
            print("Random Dice Game")
            print("1. register")
            print("2. login")
            print("3. exit")

            choice=int(input("Enter your choice: "))

            try:
                if choice == 1:
                    UserManager.register()
                elif choice ==2:
                    UserManager.login()
                elif choice == 3:
                    break
                else:
                    print("enter a number between 1-3")
            except ValueError:
                print("please enter a number")
        pass

main()



