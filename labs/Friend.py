class Friend(object):
    """
    A class that represents a friend
    """

    def __init__(self, name, friend_of, friend_level):
        # Define and initialize all the attributes that a friend will have
        self.name = name
        self.friend_level = friend_level
        self.friend_level_index = 1
        self.friend_of = friend_of

        # As we have set methods than can do other things appart of changing the value,

        # define responses based on levels in arrays
        self.salutations = ['Fuck you!',
                            'hello my friend {}. How are you?',
                            'OH MY GOD I LOVE YOU!']

        self.presentations = ['Fuck you!',
                              'hello! I am {}',
                              'OH MY GOD I LOVE YOU!']

        self.sayalls = ['Fuck you!',
                        'hello! I am {}\nhello my friend {}. How are you?',
                        'OH MY GOD I LOVE YOU!']

        # we will call it to ensure that all the behavior is done
        self.set_name(name)
        self.set_level(friend_level)

    @staticmethod
    def __convert_level_to_index(level):
        """Private method to determine the array position based on friend level
        It is marked as static, that means:
        - the method does not need to know anything about the object
        - static methods are class methods instead of object methods
        - previous points means that the method execution will be the same no matter which object uses it

        To mark a method as static, we put @staticmethod upside

        Parameters:
            level (int): the friend level to convert

        Returns:
            (int) the array position that equals to the friend level
        """
        # Default answer
        result = 1

        # Check if level is equal or lower than 2
        if level <= 2:
            # in this case, we will return the first position
            # (in python, the first position is 0)
            result = 0
        elif level >= 8:
            # in case of 8 or more, we return the last position
            result = 2

        return result

    def salutate(self):
        """This method returns a salutation

        Returns:
            (str) a salutation
        """

        return self.salutations[self.friend_level_index].format(self.friend_of)

    def present_yourself(self):
        """This method returns a presentation

        Returns:
            (str) a presentation
        """
        return self.presentations[self.friend_level_index].format(self.name)

    def say_all(self):
        """This method retuns a simple friend conversation based on a presentation and a salutation

        Returns:
            (str) simple friend conversation
        """
        return self.sayalls[self.friend_level_index].format(self.name, self.friend_of)

    def set_name(self, name):
        """Modifies the name of the friend

        Parameters:
            name (str): the new friend name
        """
        self.name = name

    def set_level(self, level):
        """Modifies the friend level

        Parameters:
            level (int): the new friend level
        """
        self.friend_level = level
        self.friend_level_index = self.__convert_level_to_index(level)
