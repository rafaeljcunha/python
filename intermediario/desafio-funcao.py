def saudacao(sds, nome):
    print(f'{sds} {nome}')


saudacao("Olá", "Rafael")


def somar(a, b, c):
    print(a + b + c)


somar(2, 3, 4)


def percent(valor, percentual):
    return valor + (valor * percentual / 100)


percentV = percent(100, 10)

print(percentV)


def fizzBuzz(valor):
    if valor % 5 == 0 and valor % 3 == 0:
        return "FizzBuzz"
    elif valor % 5 == 0:
        return "Buzz"
    elif valor % 3 == 0:
        return "Fizz"
    else:
        return valor


fizzBuzzV = fizzBuzz(30)

print(fizzBuzzV)
