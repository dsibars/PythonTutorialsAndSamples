class Friend(object):
    #Initialiser
    def __init__(self, name, friend_of, friend_level):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level

    def salute(self):
        print('Hello my friend ' + self.friend_of + '. How are you?')

    def introduce_yourself(self):
        print('Hello! I am ' + self.name)

    def say_all(self):
        self.introduce_yourself()
        self.salute()


Rodri = Friend('Rodri', 'Dani', '10')

Rodri.salute()
Rodri.introduce_yourself()

Dani = Friend('Dani', 'Rodri', '10')
Dani.salute()

Dani.say_all()