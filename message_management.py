from message import Message, ReadableMessage


class MessageManagement:

    def __init__(self):
        self.messages: list[ReadableMessage] = []

    def send_message(self, sender, receiver, message):
        new_message = ReadableMessage(sender=sender,
                                      receiver=receiver,
                                      message=message)
        self.messages.append(new_message)

    def get_user_messages(self, receiver):
        selected_list = []
        for massage in self.messages:
            if massage.get_receiver() == receiver and massage.is_read() == False:
                selected_list.append(str(massage))

        return '\n\n'.join(selected_list)
