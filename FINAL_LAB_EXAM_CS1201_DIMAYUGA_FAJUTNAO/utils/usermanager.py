from utils.dice_game import DiceGame

class UserManager:
    def load_users(self, username, password):
        self.username = {}
        self.password = {}

        pass

    def save_users():

        pass

    def validate_username():

        pass

    def validate_password():

        pass

    def register():
        username = input("Enter username: ")
        if len(username) <=3:
            print("username must be  4 charactes long")
            return
        else:
            password= input("enter password: ")
            if len(password) <=7:
                print("password must be 8 characters")
                return
            else:
                print("registration successful!")
                return
        pass

    def login():
        username = input("Enter username: ")
        if username not in username:
            print("User not found.")
            return
        password = input("enter password: ")
        if password not in password:
            print('Invalid password"')
            return
                
        print("logged in sucessful!")
        DiceGame.menu()


        pass

        