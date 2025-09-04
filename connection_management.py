import UserManagement
import User
from message import Message



class ConnectionManagement:
    users = []
    messages = []
    current_user = None

    def __init__(self):
        users = UserManagement.users
        current_user = UserManagement.get_current_user()

    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user


    def send_message(self, user_id, message):
        reciever = self.find_user(user_id)

        new_message = Message(sender=self.current_user,
                              receiver=reciever, message=message)
        self.messages.append(new_message)


    def get_messages(self, user):
        return self.messages

    def open_connect(self, user):
        user.friends.append(self.current_user)


    def close_connection(self, user):
        user.friends.remove(self.current_user)


    def get_friends(self):
        return self.current_user.friends