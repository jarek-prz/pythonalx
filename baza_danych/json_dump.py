'''
zrzucanie danych do pliku w formacie json - serializacja
'''

import json
pracownik ={
    "imie":"Jan",
    "nazwisko":"Kowalski",
    "wiek":42,
    "dostepy":['SALA01', 'SALA02', 'SALA03'],
    "wynagrodzenie": 12345.67,
    "manager":False,
    "auto":None
}

with open("pracownik.dat", "wt") as fd:
    json.dump(pracownik, fd)