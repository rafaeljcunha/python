
perguntas = {
    "Pergunta 1": {
        "pergunta": "Quantos é 2+2? ",
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'b'
    },
    "Pergunta 2": {
        "pergunta": "Quantos é 4+2? ",
        'respostas': {
            'a': '6',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'a'
    }
}

respostas_certas = 0

for pergunta_key, pergunta_value in perguntas.items():
    print(f'{pergunta_key} : {pergunta_value["pergunta"]}')

    print("Respostas:")

    for resposta_key, resposta_value in pergunta_value['respostas'].items():
        print(f'[{resposta_key}]: {resposta_value}')

    resposta_usuario = input("Informe sua resposta: ")

    if resposta_usuario == pergunta_value["resposta_certa"]:
        print("Voce acertou!")
        respostas_certas += 1
    else:
        print("Voce errou!")

        print()
print()
print(f"Voce acertou {respostas_certas} respostas de {len(perguntas)} perguntas.")
