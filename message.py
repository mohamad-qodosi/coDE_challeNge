class Message:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def get_receiver(self):
        return self.receiver

    def __str__(self):
        return f"""
        From: {self.sender}
        To: {self.receiver}
        Message: {self.message}
        """

class ReadableMessage(Message):
    def __init__(self, sender, receiver, message):
        super().__init__(sender, receiver, message)
        self.read = False

    def __str__(self):
        self.read = True
        return super().__str__()

    def is_read(self):
        return self.read
