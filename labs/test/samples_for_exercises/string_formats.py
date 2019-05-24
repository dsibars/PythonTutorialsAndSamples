# When we define a string, we can perform replacements later putting {} inside them.
# For example:
salutation = 'Hello {}, my old friend!'

# If we format the string, we can pass as many values as {} we added, and it will be replaced

print(salutation.format('potatoe'))

# We can use another variables, and store the result
name = 'persiana'
result = salutation.format(name)

print(result)

# As we mentioned before, we can use multiple variables
name2 = 'beach'
salutation_plus = 'Hey {}, I\'m glad to see you again as my {}'
result = salutation_plus.format(name, name2)

print(result)

# It's save if we pass more variables than {} we have, it simply will return the same string
noformat = 'heeeey i do not have them :('
result = noformat.format(name, name2, 'patata')
print(result)
