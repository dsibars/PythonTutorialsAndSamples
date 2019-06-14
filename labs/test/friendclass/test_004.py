import unittest
from labs.Friend import Friend


class TestFriend004(unittest.TestCase):
    def setUp(self):
        self.test_name = 'paco'
        self.test_friendof = 'meralgo'
        self.test_levels = [3, 4, 6, 7]
        self.target = Friend(self.test_name, self.test_friendof, self.test_levels[0])

        self.expected_salutate = [
            'hello my friend meralgo. How are you?', 'Whats up meralgo!']

        self.expected_present_yourself = [
            'hello! I am paco', 'You are in front of paco']

        self.expected_sayall = [
            self.expected_present_yourself[0] + '\n' + self.expected_salutate[0],
            self.expected_present_yourself[0] + '\n' + self.expected_salutate[1],
            self.expected_present_yourself[1] + '\n' + self.expected_salutate[0],
            self.expected_present_yourself[1] + '\n' + self.expected_salutate[1]
        ]

    def test_salutate(self):
        for level in self.test_levels:
            self.__test_salutate_level(level)

    def __test_salutate_level(self, level):
        self.target.set_level(level)

        first_present = False
        second_present = False

        for x in range(10):
            result = self.target.salutate()

            if result == self.expected_salutate[0]:
                first_present = True
            elif result == self.expected_salutate[1]:
                second_present = True

        self.assertTrue(first_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_salutate[0], level))
        self.assertTrue(second_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_salutate[1], level))

    def test_present_yourself(self):
        for level in self.test_levels:
            self.__test_present_yourself(level)

    def __test_present_yourself(self, level):
        self.target.set_level(level)

        first_present = False
        second_present = False

        for x in range(10):
            result = self.target.present_yourself()

            if result == self.expected_present_yourself[0]:
                first_present = True
            elif result == self.expected_present_yourself[1]:
                second_present = True

        self.assertTrue(first_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_present_yourself[0], level))
        self.assertTrue(second_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_present_yourself[1], level))

    def test_sayall(self):
        for level in self.test_levels:
            self.__test_say_all(level)

    def __test_say_all(self, level):
        self.target.set_level(level)

        first_present = False
        second_present = False
        third_present = False
        fourth_present = False

        for x in range(40):
            result = self.target.say_all()

            if result == self.expected_sayall[0]:
                first_present = True
            elif result == self.expected_sayall[1]:
                second_present = True
            elif result == self.expected_sayall[2]:
                third_present = True
            elif result == self.expected_sayall[3]:
                fourth_present = True

        self.assertTrue(first_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_sayall[0], level))
        self.assertTrue(second_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_sayall[1], level))
        self.assertTrue(third_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_sayall[2], level))
        self.assertTrue(fourth_present, 'Sentence "{}" did not appear in friend level {}'.format(self.expected_sayall[3], level))


if __name__ == '__main__':
    unittest.main()
