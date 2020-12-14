patata = 'something'
cebolla = ' else'

print(patata)


if patata == cebolla:
    print('equals')
else:
    print('not equals')





numerito1 = 69
numerito2 = 13
numerito1 = 73


numerito1entexto = str(numerito1)
print('el numerito en texto es: ' + numerito1entexto)


print(numerito1 + numerito2)
print(patata + cebolla)
print(patata + str(numerito1))


def build_with_number(text, number):
    return text + str(number)


resultat = build_with_number(patata, numerito2)

print(resultat)


def print_with_number(text, number):
    text_to_print = build_with_number(text, number)
    print(text_to_print)



print_with_number('hola ', 69)

