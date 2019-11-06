'''
zad 1
    typy danych: string, int, float, bool, complex, None

zad 2
    struktury danych: lista, tupla, set, dict

zad 3
    sortowanie listy: lista=[1,3,2]
    lista.sort()
    lista_2 = sorted(lista)

zad 4
    zwrocenie wartosci ze slownika
        slownik = {'a': 1}
        slownik['ala'] # dostaniemy wyjatek,

        trzeba np wprowadzic obsluge bledu
        try:
            slownik['ala']
        except KeyError:
            print("Brak takiego klucza")


        albo:
        slownik.get('ala') # domyslnie zwracana jest wartosc None jeżeli klucza nie ma

        albo:
        if 'ala' in slownik:
            print slownik['ala']

zad 5
    funkcja lącząca 2 napisy i odwracajace wynik
    def zlacz_teksty(a, b):
        c=a+b
        return c[::-1]


'''

#
# def zlacz_teksty(a, b):
#     c = a + b
#     return c[::-1]
#
# txt=zlacz_teksty("kobyłama", "małybok")
# print(txt)


