# print('oigas')

# string or str es una cadena de lletres

# funcions internes print i str

aparatu_gaes = 'oigas'
caca = 'cera'
print(aparatu_gaes)

Nivell_Sordesa = 1
Nivell_Sordesa2 = 2
Nivell_Sordesa3 = 3
Nivell_Sordesa4 = 4
Nivell_Sordesa5 = 5

print(Nivell_Sordesa + Nivell_Sordesa3)

print(aparatu_gaes + caca)
print(caca + str(Nivell_Sordesa3))

NivellSordesa = str(Nivell_Sordesa2)
print('el nivell de sordesa es: ' + NivellSordesa)

# afegir més funcions, relacionades amb tot això. Com a entrada tindra dos variables, primera de text y segona d enumero, y el que fara sera imprimirte el texte y el numero

# com definir funcio en python

def build_with_number(text, number):
    return text + str(number)


resultat = build_with_number(caca, Nivell_Sordesa4)

print(resultat)

def print_with_number(text, number):
    text_to_print = build_with_number(text, number)
    print(text_to_print)



print_with_number('hola ', 5)
print_with_number(caca, Nivell_Sordesa4)


print_with_number('hola ', 5)

# Modify values

caca += ' líquida'
print(caca)
