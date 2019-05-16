import unittest
from labs.Friend import Friend

# EXERCISE:
# Create a new function in friend, that allows you to change the level.
# When the level is 2 or lower, all functions has to say 'Fuck you!'
# When the level is 8 os higher, all functions has to say 'OH MY GOD I LOVE YOU!'


class TestFriend003(unittest.TestCase):
    def setUp(self):
        self.test_name = 'patata'
        self.test_friendof = 'cebolla'
        self.test_level = 5
        self.target = Friend(self.test_name, self.test_friendof, self.test_level)

    def test_friend_level_low(self):
        # Test friend level to low value
        test_new_level = 2

        # Set a new level
        self.target.set_level(test_new_level)

        # Expected result
        expected_result = 'Fuck you!'

        # Generate the result
        result1 = self.target.present_yourself()
        result2 = self.target.salutate()
        result3 = self.target.say_all()

        # Restore the level
        self.target.set_level(self.test_level)

        # Check if the expected result and result are the same
        self.assertEquals(result1, expected_result)
        self.assertEquals(result2, expected_result)
        self.assertEquals(result3, expected_result)

    def test_friend_level_high(self):
        # Test friend level to low value
        test_new_level = 8

        # Set a new level
        self.target.set_level(test_new_level)

        # Expected result
        expected_result = 'OH MY GOD I LOVE YOU!'

        # Generate the result
        result1 = self.target.present_yourself()
        result2 = self.target.salutate()
        result3 = self.target.say_all()

        # Restore the level
        self.target.set_level(self.test_level)

        # Check if the expected result and result are the same
        self.assertEquals(result1, expected_result)
        self.assertEquals(result2, expected_result)
        self.assertEquals(result3, expected_result)


if __name__ == '__main__':
    unittest.main()
