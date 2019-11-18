# przyjmowanie przez funkcję dowolnej liczby argumentów

# funkcja mnozy wartosci podane do jej środka
# możliwe podanie nieznanej liczby parametrów
# musi być na początku gwiazdka * i po niej dowolna nazwa zwyczajowo args, ale moze byc inna. W wejsciu do funkcji będzier to lista
# jeżeli ma być parametr obowiązkowy to musi byc na początku
def iloczyn(start, *args):
    wynik=start
    for nr, arg in enumerate(args,1):
        wynik*=arg
        print(f"Pozycja {nr} = {arg}")
    print(f"Iloczyn = {wynik}")

iloczyn(0,1,2,3,4)


