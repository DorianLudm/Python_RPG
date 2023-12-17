class User:
    def __init__(self):
        self.logined = False
        self.username = None
    
    def login(self, username):
        self.logined = True
        self.username = username
    
    def logout(self):
        self.logined = False
        self.username = None

    def __repr__(self) -> str:
        return f'User({self.username}, {self.logined})'