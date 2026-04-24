class login_system:
      def __init__(self):
        self.users={}

      def sign_up(self):
        username=input("enter user name:")
        password=input("enter password:")
        self.users[username]=password
        print("signup successful!!!")

      def login(self):
        if not self.users:
            print("please signup first!!!")
            return
        
        attempts=3
        while attempts > 0:
           username=input("enter username:")
           password=input("enter password:")
           if username in self.users and self.users[username]==password:
            print("login successful!!!")
            return
           else:
            attempts-=1
            print(f" Wrong credentials. Attempts left: {attempts}")
        print("account locked too many failed attempts!!!")

      def menu(self):
            while True:
             print("\n1.signup \n2.login\n3.exit") 
             try:
                choice=int(input("enter your choice:"))   
             except ValueError:
                print("please enter a valid input!!!")
                continue
             if choice==1:
                self.sign_up()
             elif choice==2:
                self.login()
             elif choice==3:
            #     self.menu()
            #  elif choice==4:   
                print("exit the program!!!") 
                break
             else:
                print("invalid choice!!!")
                
login=login_system()
login.menu()

             
      