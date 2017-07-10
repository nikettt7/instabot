APP_ACCESS_TOKEN = '2280536012.dfab058.1e90d0f8b510437989565c370545926b'


from datetime import datetime


# Let us create a spy class that contains our very own spy and his friends
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('Apoorav', 'Mr.', 20, 4.5)

friend_one = Spy('pranjal', 'Mr.', 29, 4.5)
friend_two = Spy('prableen', 'Ms.', 35, 5.0)
friend_three = Spy('ekjot', 'Dr.', 19, 6.0)

friends = [friend_one, friend_two, friend_three]

