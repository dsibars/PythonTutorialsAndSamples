# print i str son funcions de Python

# print('coca')
# print('clenxes FC')

material_clenxil = 'keta'
material_sa = 'tofu'

#print(material_clenxil)

clenxes_matinals = 2
clenxes_nocturnes = 6

clenxitext = str(clenxes_matinals)

#print(clenxes_matinals + clenxes_nocturnes)
#print(material_clenxil + material_sa)

print(material_sa + ': ' + clenxitext)

def build_with_number(text, number):
    return text + str(number)

sumada = build_with_number(material_clenxil, clenxes_matinals)

print(sumada)

def print_with_number(text, number):
    print(text + str(number))

print_with_number(material_sa, clenxes_nocturnes)
