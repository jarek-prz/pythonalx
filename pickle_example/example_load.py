import pickle

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

with open("osoby.pickle", 'rb') as f:
    dane = pickle.load(f)

print(dane.imie, dane.wiek)