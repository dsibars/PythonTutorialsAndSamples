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
        # Test change name functionality
        test_new_name = 'petete'
        # Set a new name
        self.target.set_name(test_new_name)
        # Expected result
        expected_result = 'hello! I am ' + test_new_name
        # Generate the result
        result = self.target.present_yourself()
        # Restore the name
        self.target.set_name(self.test_name)

        # Check if the expected result and result are the same
        self.assertEquals(result, expected_result)


if __name__ == '__main__':
    unittest.main()
