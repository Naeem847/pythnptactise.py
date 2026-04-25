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
           print("log_in successful")
        else:
            print("you entered the wrong username or password")
    def menu(self):


     while True:

            print("\n1. sign_up\n2. log_in,\n3. exit")
            choice=int(input("enter your coice:"))

            if choice==1:
                self.sign_up()
            elif choice==2:
                self.log_in()
            elif choice==3:
                break
            else:
                print("invalid choice")


login = LoginSystem()
login.menu()