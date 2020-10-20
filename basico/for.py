texto = 'Python'

for index, letra in enumerate(texto):
    print(index, letra)
print('####################')
for numero in range(10):
    print(numero)
print('####################')
for n in range(20, 10, -1):
    print(n)
print('####################')

nova_string = ""

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
