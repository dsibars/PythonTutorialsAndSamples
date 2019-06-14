from random import *


class Friend(object):
    """
    A class that represents a friend
    """

    MIN_STANDARD_LEVEL = 3
    MAX_STANDARD_LEVEL = 7
    AVERAGE_LEVEL = 5

    def __init__(self, name, friend_of, friend_level):
        # Define and initialize all the attributes that a friend will have
        self.name = name
        self.friend_level = friend_level
        self.friend_of = friend_of

        # define responses based on levels in arrays
        self.salutations = ['Fuck you!',
                            'hello my friend {}. How are you?',
                            'Whats up {}!',
                            'OH MY GOD I LOVE YOU!']

        self.presentations = ['Fuck you!',
                              'hello! I am {}',
                              'You are in front of {}',
                              'OH MY GOD I LOVE YOU!']

        # As we have set methods than can do other things appart of changing the value,
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
        result = randint(1, 2)

        # Check if level is equal or lower than 2
        if level < Friend.MIN_STANDARD_LEVEL:
            # in this case, we will return the first position
            # (in python, the first position is 0)
            result = 0
        elif level > Friend.MAX_STANDARD_LEVEL:
            # in case of 8 or more, we return the last position
            result = 3
        elif level == Friend.AVERAGE_LEVEL:
            result = 1

        return result

    def salutate(self):
        """This method returns a salutation

        Returns:
            (str) a salutation
        """
        friend_level_index = Friend.__convert_level_to_index(self.friend_level)
        return self.salutations[friend_level_index].format(self.friend_of)

    def present_yourself(self):
        """This method returns a presentation

        Returns:
            (str) a presentation
        """
        friend_level_index = Friend.__convert_level_to_index(self.friend_level)
        return self.presentations[friend_level_index].format(self.name)

    def say_all(self):
        """This method retuns a simple friend conversation based on a presentation and a salutation

        Returns:
            (str) simple friend conversation
        """
        if self.friend_level < Friend.MIN_STANDARD_LEVEL or self.friend_level > Friend.MAX_STANDARD_LEVEL:
            result = self.salutate()
        else:
            result = self.present_yourself() + '\n' + self.salutate()

        return result

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
