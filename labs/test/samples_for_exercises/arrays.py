# Arrays are a list of elements, and we can define it with []
myfirstlist = []

# TO add an element, we use the method append
myfirstlist.append('hello')

# Check the array size, we use the global len method
size = len(myfirstlist)

print(str(size))

# let's add some more elements
myfirstlist.append('hi')
myfirstlist.append('yuhuuu')

# To access a position of the array, we use a number begining from 0.
# First element
print(myfirstlist[0])

# Second element
print(myfirstlist[1])

# Third and last element
print(myfirstlist[2])

# THe append methods adds the element to the last position, but we can also insert at the position we want
# Insert an element at the beginning (position 0)
myfirstlist.insert(0, 'hooolaaaa')

# now the first element will be the new string inserted
# First element
print(myfirstlist[0])

# With this, we delete all elements and reset the array
myfirstlist.clear()

# We can do a lot of thing with arrays, like sorting, removing certain elements etc. It's your work to google it! :)
