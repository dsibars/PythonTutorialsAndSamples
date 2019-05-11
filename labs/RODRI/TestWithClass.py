# OOP

# Create a class with functionality


class Friend(object):
    def __init__(self, name, friend_of, friend_level):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level

    def salutate(self):
        print('hello my friend' + ', ' + self.friend_of + '. How are you?')

    def present_yourself(self):
        print('hello! I am ' + self.name)

    def say_all(self):
        self.present_yourself()
        self.salutate()



dani = Friend('Dani', 'Rodri', 10)

dani.present_yourself()
dani.salutate()

charly = Friend('Charly', 'Rodri', 10)
charly.present_yourself()
charly.salutate()



