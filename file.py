import os
import pickle

class Saver:
    def __init__(self, connection_management, message, readable_message):
        self.connection_management = connection_management
        self.message = message
        self.readable_message = readable_message

    def __str__(self):
        return f"[{self.connection_management}] {self.message} - {self.readable_message}"
    
    @staticmethod
    def save(file_name, obj_list):
        with open(file_name, "wb") as f:
            pickle.dump(obj_list, f)

    @classmethod
    def save_messages(cls, messages_list):
        cls.save('messages.pkl', messages_list)

    @classmethod
    def save_connection_managements(cls, connection_managements_list):
        cls.save('connection_managements.pkl', connection_managements_list)

    @classmethod
    def save_readable_messages(cls,readable_messages_list):
        cls.save('readable_message.pkl', readable_messages_list)

class Loader:
    def __init__(self, connection_management, message, readable_message):
        self.connection_management = connection_management
        self.message = message
        self.readable_message = readable_message
        
    @staticmethod
    def open_file(file_name: str) -> list:
        if os.path.exists(file_name):
            with open(file_name, "rb") as f:
                my_obj_list = pickle.load(f)
            
            return my_obj_list
        else:
            return []

    @classmethod
    def load_messages(cls):
        return cls.open_file('messages.pkl')
    
    @classmethod
    def load_connection_managements(cls):
        return cls.open_file('connection_managements.pkl')
    
    @classmethod
    def load_readable_messages(cls):
        return cls.open_file('readable_messages.pkl')

        
                
if __name__ == "__main__":
    class MyClass:
        def __init__(self, value):
            self.value = value
        def print_value(self):
            print(self.value)

    obj_list = [MyClass(1), MyClass(2)]
    
    Saver.save_messages(obj_list)
    objs = Loader.load_messages()
    for obj in objs:
        obj.print_value()
        
    objs = Loader.load_connection_managements()
    print(objs)
    