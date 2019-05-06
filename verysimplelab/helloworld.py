# prints something
print('hello!')

# creates a variable that contains the data to print
text = 'hello world'

# print the variable value
print(text)


# Define a number
number = 1

# Print combination
print(text + str(number))

# Modify values
text = 'hey you! hello'
number = 2

print(text + str(number))

# Modify values appending at the end
text += ' again'
number+=1

print(text + str(number))

# Print in a more visual mode the data
print('current text is: ' + text)
print('current number is: ' + str(number))
print('all together: ' + text + str(number))

# The last print can be used several times... let's create a function
def myCustomPrint(text, number):
    print('current text is: ' + text)
    print('current number is: ' + str(number))
    print('all together: ' + text + str(number))


# Let's try! this should do the same
myCustomPrint(text, number)

# We can harcode another values
myCustomPrint('patata', 54454)


# Create a class with functionality :D

class MyPrinter(object):
    # Initializer / Instance Attributes
    def __init__(self, text, number):
        self.text = text
        self.number = number

    def buildAllTogetherText(self, text, number):
        return 'all together: ' + text + str(number);

    def myCustomPrint(self, text, number):
        print('current text is: ' + text)
        print('current number is: ' + str(number))
        print('all together: ' + self.buildAllTogetherText(text, number))

    def print(self):
        self.myCustomPrint(self.text, self.number)

    def getAllTogetherText(self):
        return self.buildAllTogetherText(self.text, self.number)

    def increase(self):
        self.number += 1


printer = MyPrinter('pipas', 69)

print(printer.getAllTogetherText())
print(printer.buildAllTogetherText('aaaannnnn', 44))

printer.myCustomPrint('yuhuu', 'yeheeee')

printer.print()





