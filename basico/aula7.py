nome = "Rafael"
idade = 27
altura = 1.73
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idades e seu imc é', imc, sep=' ')

print(f"{nome} tem {idade} de idades e seu imc é {imc:.2f}")
print("{} tem {} de idades e seu imc é {:.2f}".format(nome, idade, imc))
print("{n} tem {i} de idades e seu imc é {im:.2f}".format(n=nome, i=idade, im=imc))
