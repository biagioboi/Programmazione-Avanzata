import abc

class User(metaclass=abc.ABCMeta):
    def __init__(self, med, name):
        self.mediator = med
        self.name = name

    @abc.abstractmethod
    def send(self, msg):
        pass

    @abc.abstractmethod
    def receive(self, msg):
        pass

class ChatMediatorImpl:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, user, message):
        for u in self.users:
            if u != user:
                u.receive(message)

class UserImpl(User):
    def send(self, msg):
        print(self.name + ": Invio messaggio: " + msg)
        self.mediator.send_message(self, msg)

    def receive(self, msg):
        print(self.name + ": Messaggio ricevuto: " + msg)

if __name__ == '__main__':
    mediator = ChatMediatorImpl()
    user1 = UserImpl(mediator, "John")
    user2 = UserImpl(mediator, "Lisa")
    user3 = UserImpl(mediator, "Maria")
    user4 = UserImpl(mediator, "David")
    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    mediator.add_user(user4)

    user1.send("Hi All")
