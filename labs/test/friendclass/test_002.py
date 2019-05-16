import unittest
from labs.Friend import Friend

# EXERCISE:
# Create a new function in friend, that allows you to change the name.
# Tests will check that after changing the name, the salutate method has the new name.


class TestFriend002(unittest.TestCase):
    def setUp(self):
        self.test_name = 'patata'
        self.test_friendof = 'cebolla'
        self.test_level = 5
        self.target = Friend(self.test_name, self.test_friendof, self.test_level)

    def test_change_name(self):
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
