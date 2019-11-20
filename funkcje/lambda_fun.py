"""
funkcje anonimowe
"""

x=lambda a,b : a*b

print(x(10,6))


lista = [('Jabłko',2.99), ("Banan", 1.50), ("Winogrona", 4.20)]


def fun_sort(x):
    return x[1]
    pass


print(sorted(lista, key=fun_sort))
print(sorted(lista, key=lambda x:x[1]))






