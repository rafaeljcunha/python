palavra = input("Digite a palavra secreta: ")
palavra = palavra.upper()
letras_digitadas = []
acertou = False

while True:
    letra = input("Digite uma letra: ")
    letra = letra.upper()

    if len(letra) > 1:
        print("Você deve digitar apenas uma letra.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra:
        print("==== Você acertou uma letra!!! ====")
    else:
        print(f'!!!! A letra "{letra}" não existe na palavra secreta. !!!!')
        letras_digitadas.pop()

    letras_temporarias = ""

    for letra_secreta in palavra:
        if letra_secreta in letras_digitadas:
            letras_temporarias += letra_secreta
        else:
            letras_temporarias += "*"

    print(letras_temporarias)

    if palavra == letras_temporarias:
        acertou = True
        print(f"#### Você acertou e a palavra é {letras_temporarias} ####")
        if acertou:
            palavra = ''
            letras_temporarias = ''
            letras_digitadas = []
            sair = input("Deseja sair? [S]im ou [N]ão: ")
            sair = sair.upper()
            if sair == "S":
                break
            else:
                nova_palavra = input("Digite uma nova palavra: ")
                palavra = nova_palavra.upper()
                continue
