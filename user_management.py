from file import Loader, Saver

class User_management():

    def __init__(self):
        self.users_list = Loader.load_users()
        self.current_user = None
        
    def add_user(self, user):
        self.users_list.append(user)
        Saver.save_users(self.users_list)
     
    def find_user(self, username):
        for user in self.users_list :
            if user.get_username() == username:
                return user
        return None
                
     
    def sing_up_user(self, username, password):
        if self.find_user(username):
            return False
        
        new_user = User(username, password)
        self.add_user(new_user) 
        return True      
        
     
        
    def login_user(self, username, password) :
        for user in self.users_list :
            if user.authentication(username, password):
                self.current_user = user
                return user
        return None



class User:

    def __init__(self , username, password) :
        self.username = username
        self.password = password

    def authentication(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False 
        
    def get_username(self):
        return self.username
