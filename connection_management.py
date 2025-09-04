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


    def send_message(self, user_id, message):
        receiver = UserManagement.find_user(user_id)

        new_message = Message(sender=self.current_user,
                              receiver=receiver, message=message)
        self.messages.append(new_message)


    def get_messages(self, user):
        return self.messages

    def open_connect(self, user):
        user.friends.append(self.current_user)


    def close_connection(self, user):
        user.friends.remove(self.current_user)


    def get_friends(self):
        return self.current_user.friends