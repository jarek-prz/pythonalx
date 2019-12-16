'''
baza danych pracowników
'''

# informacje o pracownikach

import datetime
import json

dane_pracownikow = list()

try:
    with open("pracownicy.dat", "rt") as fd:
        json.load( fd)
except:
    print("Odczyt pliku nie udał się.")

def wprowadz_dane():
    print('='*40)
    print("Wprowadź dane pracownika")

    imie = None
    naswisko = None
    rok_urodzenia = None
    pensja = None

    while(True):
        imie = input("Podaj imię: ").upper().strip()
        if len(imie)>=3:
            break

    while(True):
        nazwisko = input("Podaj nazwisko: ").upper().strip()
        if len(nazwisko)>=3:
            break

    while True:
        try:
            rok_urodzenia = int(input("Podaj rok urodzenia: ").strip())
            if rok_urodzenia<1930:
                print("Idź na emeryturę.")
                continue
            rok_biezacy = datetime.datetime.now().year
            if rok_biezacy-rok_urodzenia>=15:
                break
            print("Za młodyś na pracę.")
        except Exception as exc:
            print("Podaj rok urodzenia", exc)


    while True:
        try:
            pensja = float(input("Podaj wartość wynagrodzenia: "))
            if pensja>0:
                break
            print("Podaj wartosć wynagrodzenia")
        except Exception as exc:
            print("Podaj wartosć wynagrodzenia", exc)

    return("imie:", imie, "nazwisko:", nazwisko, "rok_urodzenia:", rok_urodzenia, "pensja:", pensja)

def pokaz_rekordy():
    print("====== LISTA PRACOWNIKÓW ========")
    if len(dane_pracownikow)==0:
        print("Brak danych")
        return
    for rekord in dane_pracownikow:
        print(f"{rekord.get('imie')}\t{rekord.get('nazwisko')}\t{rekord.get('rok_urodzenia')}\t{rekord.get('pensja')}")


while(True):
    operacja  = input("Podaj operację [d/w/q] ").strip().upper()
    if operacja == "Q":
        break

    if operacja == "W":
        pokaz_rekordy()

    if operacja == "D":
        # prosimy o dane
        rekord = wprowadz_dane()
        dane_pracownikow.append(rekord)
        with open("pracownicy.dat", "wt") as fd:
            json.dump(rekord, fd)

