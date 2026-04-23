class LoginSystem:


    def __init__(self):
        self.users={}
    def sign_up(self):


        username=input("enter username:")
        userpassword=input("enter the password:")
        self.users[username]=userpassword
        print("sign_up successful")
    def log_in(self):


        username=input("enter username:")
        password=input("enter the password:")
        if username in self.users and self.users[username]==password:       
