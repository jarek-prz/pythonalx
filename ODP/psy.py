
# definicja klasy
class Pies:

    gatunek="Burek"
    ile=0

    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga
        Pies.ile +=1

    def szczekaj(self):
        print(f"{self.imie} szczeka")

    @classmethod
    def incr(cls):
        print(f"{self.imie}")

    pass


# tworzę instancję klasy Pies, przypisaną do zmiennej azor
azor=Pies("Azor", 10)
azor.szczekaj()


#print(azor)
#print(isinstance(azor, Pies))
#print(dir(azor))

#print(isinstance(azor, object))

#azor.waga=10
#azor.waga+=1

#print(azor==rex)
