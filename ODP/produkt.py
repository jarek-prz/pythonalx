'''
utworz klase Produkt
ktora bedzie dzialac ta, ze np
pr=Produkt(1, "woda", 10.99)

pr.id=1
pr.name="woda"
pr.price=10.99

metoda pr.show()

'''

# definicja klasy
class Produkt:
    _NEXT_ID = 1

    def __init__(self, name, price):
        #self.id = id
        self.name = name
        self.price = price
        self.id=Produkt._NEXT_ID

    @classmethod
    def incr_next_id(cls):
        cls._NEXT_ID+=1

    @classmethod
    def get_id(cls):
        return cls._NEXT_ID


    def show(self):
        return (f" {self.name} ({self._NEXT_ID}), cena: {self.price}")
    pass

pr = Produkt( "Woda", 10.99)
pr.show(pr.id)





