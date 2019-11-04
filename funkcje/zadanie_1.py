# funkcja ktora sprawdzi czy podana liuczba kest liczba pierwsza

import unittest



def czy_pierwsza(x):
    """Sprawdza, czy x jest liczbą pierwszą
    Przykłąd użycia doctestów
    Ten obszar nazywa się docstring i sluzy do tworzenia dokumentacji funkcji
    >>> czy_pierwsza(7)
    True
    >>> czy_pierwsza(10)
    False
    """
    for liczba in range(2,x): # do x i tak nie dochodzi
        if x % liczba == 0:
            wynik="- To nie jest liczba pierwsza"
            return False
        wynik = "- To jest liczba pierwsza"
    return True



#print(7, czy_pierwsza(7))
#print(10, czy_pierwsza(10))
#print(help(czy_pierwsza))

#testy
#prymitywna forma testów bez żadngo frameworka
#assert czy_pierwsza(7) is True
#assert czy_pierwsza(10) is True

# python -m doctest zadanie_1.py
# python -m unittest zadanie_1.py

class TestCzyPierwsza(unittest.TestCase):
    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_pierwsza(5), True)
        self.assertEqual(czy_pierwsza(7),  True)

    def test_czy_pierwsza_dla_liczby_niepierwszej(self):
        self.assertEqual(czy_pierwsza(10),  False)
        self.assertEqual(czy_pierwsza(12),  False)


# pip install pytest - dziala w pythonie 3.8.0
def test_czy_pierwsza_dla_liczby_pierwszej(self):
    assert czy_pierwsza(5) is True
    assert czy_pierwsza(7) is True

def test_czy_pierwsza_dla_liczby_niepierwszej(self):
    assert czy_pierwsza(10) is True
    assert czy_pierwsza(7) is True