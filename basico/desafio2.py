num1 = input("Digite um numero inteiro: ")

if num1.isnumeric():
    num1 = int(num1) % 2 == 0
    if num1:
        print(f"Você digitou número inteiro, e ele é par")
    else:
        print(f"Você digitou número inteiro, e ele é impar")
else:
    print("Você não digitou um numero inteiro!")


horario = input("Digite um horario (0-23): ")

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("O horario deve estar entre 0 e 23")
    else:
        if horario >= 0 and horario <= 11:
            print("Bom dia")
        elif horario >= 12 and horario <= 17:
            print("Boa tarde")
        else:
            print("Boa noite")
else:
    print("Por favor, digite um horario entre 0 e 23")


nome = input("Digite o seu nome")

tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")
