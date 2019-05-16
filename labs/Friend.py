class Friend(object):
    def __init__(self, name, friend_of, friend_level):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level

    def salutate(self):
        return 'hello my friend ' + self.friend_of + '. How are you?'

    def present_yourself(self):
        return 'hello! I am ' + self.name

    def say_all(self):
        return self.present_yourself() + '\n' + self.salutate()
