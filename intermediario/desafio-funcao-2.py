def sobFunc(func, msg):
    func(msg)


def func(msgS):
    print(msgS)


sobFunc(func, "Olá")


def funcao1(func, msg, num1, num2, num3):
    funcao2(msg)
    print(funcao3(num1))
    print(funcao4(num2, num3))


def funcao2(msgS):
    print(msgS)


def funcao3(num1):
    return num1


def funcao4(num1, num2):
    return num1 + num2


funcao1(funcao2, "ola funcao 2", 3, 4, 5)
