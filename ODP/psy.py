
# definicja klasy
class Pies:
    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga

    def szczekaj(self):
        print(f"{self.imie} szczeka")
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
