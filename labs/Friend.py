import sys


class Friend(object):
    def __init__(self, name, friend_of, friend_level):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level


#    def set_level(self, newlevel):
#        self.friend_level = newlevel
#
#    if self.friend_level >= 8:
#        print('OH MY GOD I LOVE YOU!')
#        sys.exit() #talla el rollo ( no se com es diu aquesta funcio)
#    if self.friend_level <= 3:
#        print('Fuck you!')
#        sys.exit() #talla el rollo ( no se com es diu aquesta funcio)


    def set_name(self, newname):
        self.name = newname

    def salutate(self):
        return 'hello my friend ' + self.friend_of + '. How are you?'

    def present_yourself(self):
        return 'hello! I am ' + self.name

    def say_all(self):
        return self.present_yourself() + '\n' + self.salutate()

