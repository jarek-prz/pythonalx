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

# moze byc wiele return'ow; ale funkcja sie konczy po napotkaniu pierwszego return

def do_potegi(podstawa, wykladnik):
    return podstawa**wykladnik

print(do_potegi(2,16))

# mozna tez zwracac wiecej, niz 1 element
# wtedy w wyniku dostajemy tuplę
def unique_letters(tekst):
    u_letters = set(tekst)
    u_letters = "".join(u_letters)
    return u_letters, len(tekst)


print(unique_letters("ala ma kota"))