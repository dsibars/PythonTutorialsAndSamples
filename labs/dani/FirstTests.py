patata = 'something'
cebolla = ' else'

print(patata)

numerito1 = 69
numerito2 = 133

numerito1entexto = str(numerito1)
print('el numerito en texto es: ' + numerito1entexto)


print(numerito1 + numerito2)
print(patata + cebolla)
print(patata + str(numerito1))


def print_with_number(text, number):
    print(text + str(number))


print_with_number('hola ', 69)

