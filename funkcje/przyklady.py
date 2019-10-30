# definicja funkcji, procedury, zestawu instrukcji
def nazwa_funkcji(): # ta funkcja nie przyjmuje żadnych argumentow
    # ciao funkcji
    print("Hello funkcja 1")
    pass

x= nazwa_funkcji
# wywołanie
x()

def do_piatej(liczba):
   # print(liczba^5)
    x= liczba**5
    return x

print(do_piatej(2))


# funkcja ktora przyjmuje napois i zwraca ten tekst ale w samych duzych literach
def na_duze_litery(napis):
    x= napis.upper()
    return x

print(na_duze_litery("Ale ma kota!"))