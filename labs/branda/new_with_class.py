class Friend(object):
    #Initialiser
    def __init__(self, name, friend_of, friend_level, sexuality):
        self.name = name
        self.friend_of = friend_of
        self.friend_level = friend_level
        self.sexuality = sexuality
        self.attracted()
        #self.gender = gender

    def salute(self):
        print('Hello my friend ' + self.friend_of + '. How are you?')

    def introduce_yourself(self):
        print('Hello! I am ' + self.name)

    def say_all(self):
        self.introduce_yourself()
        self.salute()

    def attracted(self):
        if self.sexuality == 'homo' or 'gay' or 'homosexual' or 'bi' or 'bisexual':
            return 'cachonder'
        else:
            return 'flaccid'

    def follamiguejada(self):
        print('Love is in the air. ' + self.name + ' gently caresses ' + self.friend_of + 's soft hair before leaning in for a kiss.' )
        if self.attracted() == 'cachonder':
            print('As he does so, ' + self.name + ' says: ' + self.friend_of + ', I really want you inside tonight.')
        else:
            print( self.name + ' and ' + self.friend_of + ' melt in a hug, as they promise each other eternal friendship in a totally not sexual moment.')


Rodri = Friend('Rodri', 'Dani', '10', 'hetero')

Rodri.salute()
Rodri.introduce_yourself()

Dani = Friend('Dani', 'Rodri', '10', 'asexual')
Dani.salute()

Dani.say_all()

Lorenzo = Friend('Lorenzo', 'Dani', '1', 'homo')
Lorenzo.say_all()

Rodri.follamiguejada()

Lorenzo.follamiguejada()

