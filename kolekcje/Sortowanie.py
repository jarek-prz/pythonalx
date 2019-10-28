lista = [5,10,0,-1,200,14]

# sortowanie 1 sposob - nie zmioenia wyjsciowej listy
print(lista)
print(sorted(lista))
print(lista)

# 2 sposob - zmienia listę wyjściową (zmienia stan listy
print(lista)
print(lista.sort())
print(lista)

# pozwala na dodanie dodatkowego partametru reverse

# sortowanie 1 sposob - nie zmioenia wyjsciowej listy
print(lista)
print(sorted(lista, reverse=True))
print(lista)

# 2 sposob - zmienia listę wyjściową (zmienia stan listy
print(lista)
print(lista.sort( reverse=True))
print(lista)

# sortowanie zbioru set
# sortuje i wynik zmienia na listę
zbior = {5,10,0,-1,200,14}
print(sorted(zbior))

# jeżeli lista ma w sobie wartości liczbowe i nuymeryczne - wychodzi błąd


