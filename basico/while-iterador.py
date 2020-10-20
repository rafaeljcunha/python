frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
nova_string = ''
contador = 0

input_do_usuario = input("Qual letra deseja colocar maiúscula? ")

# Iteração <- Iterar, percorrer algo
while contador < tamanho:
    letra = frase[contador]

    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
