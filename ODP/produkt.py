'''
utworz klase Produkt
ktora bedzie dzialac ta, ze np
pr=Produkt(1, "woda", 10.99)

pr.id=1
pr.name="woda"
pr.price=10.99

metoda pr.show()
>>> from produkt import Produkt
>>> pr = Produkt(1, "Woda", 10.99)
>>> pr.show()
>>> "Woda (1) cena: 10.99"
'''

# definicja klasy
class Produkt:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        return (f" {self.name} ({self.id}), cena: {self.price}")
    pass

#pr = Produkt(1, "Woda", 10.99)
#pr.show()

def test_produkt():
    pr = Produkt(1, "Woda", 10.99)
    assert pr.id == 1
    assert pr.name == "Woda"
    assert pr.price == 10.99

def test_produkt_show():
    pr = Produkt(1, "Woda", 10.99)
    assert pr.show()== "Woda (1), cena: 10.99"