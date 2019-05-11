class Friend(object):
    def __init__(self, name, friend_of, friend_level):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level

    def salutate(self):
        print('hello my friend ' + self.friend_of + '. How are you?')

    def present_yourself(self):
        print('hello! I am ' + self.name)

    def say_all(self):
        self.present_yourself()
        self.salutate()


rodri = Friend('Rodri', 'dani', 10)

rodri.present_yourself()
rodri.salutate()

branda = Friend('branda', 'dani', 10)

branda.present_yourself()
branda.salutate()


lorenzo = Friend('loreno','dani',1)

lorenzo.say_all()
