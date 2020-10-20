from random import randint

randNumber = str(randint(100000000, 999999999))
generateCpf = randNumber
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(generateCpf[index]) * reverse

    reverse -= 1

    if reverse < 2:
        reverse = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0

        total = 0
        generateCpf += str(digito)

print(generateCpf)
