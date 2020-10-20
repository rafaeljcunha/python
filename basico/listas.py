"""
Fatiamento
append, insert, pop, del
clear, extend, +, min, max, range
"""
lista = ['A', 'B', 'C', 'D', 10]
lista[4] = 'Dez'

print(lista[4])

print(lista[0:3])

print(lista[:4])

print(lista[::-1])


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l3)

l1.extend(l2)
l1.extend('t')

print(l1)

l2.append('b')
l2.insert(0, 'banana')

print(l2)
