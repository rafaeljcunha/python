nome: str = 'Rafael'
idade: int = 27
altura: float = 1.73
peso: float = 78.0
nasceu: int = 2020 - idade
imc: float = peso / (altura ** 2)

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc}.")
print(f"{nome} nasceu em {nasceu}.")
