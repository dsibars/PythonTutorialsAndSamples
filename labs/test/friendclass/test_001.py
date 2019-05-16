import unittest
from labs.Friend import Friend


class TestFriend001(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
