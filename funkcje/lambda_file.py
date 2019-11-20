# wybranie elementów okreslonych przez funkcję klucza
# raczej filter
lista = [1,2,3,4,5,6]

result = list(filter(lambda x: x>=4, lista))
print(result)

def wybierz(lista, funkcja):
    wynik=[]
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
    return wynik

lista_2 = wybierz(lista, lambda x: x%3 ==0)
print(lista_2)


# funkcja z 2 funkcjami jako argumenty
def przytnij (lista, start, stop):
    wynik=[]
    czy_dodawac=False
    for el in lista:
        if start(el):
            czy_dodawac = True
        if czy_dodawac == True:
            wynik.append(el)
        if stop(el):
            break
    return wynik

lista = [1,2,3,4,5,6,7]

start = lambda x: x>4
stop = lambda x: x==6

lista_2 = przytnij(lista, start, stop)
print(lista_2)

def test_przytnij():
    result=przytnij(
        lista=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 4,
        stop = lambda x: x == 6
    )
    assert result == [5, 6]




