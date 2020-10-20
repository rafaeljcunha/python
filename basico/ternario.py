idade = 17
msg = "Maior de idade" if idade >= 18 else "Menor de idade"

print(msg)

nome = input("Qual o seu nome? ")
print(nome or "Você não informou seu nome!")


a = 0
b = None
c = False
d = []
e = {}
f = 27
g = 'Rafael'

conditionOR = a or b or c or d or e or f or g

print(conditionOR)
