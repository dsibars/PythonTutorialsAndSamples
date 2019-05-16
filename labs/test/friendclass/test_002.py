import unittest
from labs.Friend import Friend

# EXERCISE:
# Create a new function in friend, that allows you to change the name.
# Tests will check that after changing the name, the salutate method has the new name


class TestFriend002(unittest.TestCase):
    def setUp(self):
        self.test_name = 'patata'
        self.test_friendof = 'cebolla'
        self.test_level = 5
        self.target = Friend(self.test_name, self.test_friendof, self.test_level)

    def test_salutate(self):
        expected_result = 'hello my friend ' + self.test_friendof + '. How are you?'
        self.assertEquals(self.target.salutate(), expected_result)

    def test_present_yourself(self):
        expected_result = 'hello! I am ' + self.test_name
        self.assertEquals(self.target.present_yourself(), expected_result)

    def test_say_all(self):
        expected_result = 'hello! I am ' + self.test_name + '\n' + 'hello my friend ' + self.test_friendof + '. How are you?'
        self.assertEquals(self.target.say_all(), expected_result)

    def change_name(self):
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
        self.assertEquals(self.target.present_yourself(), expected_result)


if __name__ == '__main__':
    unittest.main()
