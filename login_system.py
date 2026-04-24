class LoginSystem:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self):
        try:
            user = input("Username: ")
            pwd = input("Password: ")

            if user != self.username or pwd != self.password:
                raise Exception("Wrong credentials")

            print("Login successful")
        except Exception as e:
            print("Error:",e)

login = LoginSystem()
login.login()