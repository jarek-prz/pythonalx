# przekazywanie listy parametrów nazwanych
# piszemy ** i nazwa zwyczajowo używana "kwargs"
# ** konwertuje nam przekazane parametry do słownika

def fun_parametry(nr, **kwargs):
    print("Imię: ", kwargs.get("imie", "brak-"))
    print(kwargs)

fun_parametry(102, imie="Jan", nazwisko="Kowalski", email="jan.kowalski@firma.pl", wiek=44)