# tworzenie rekordu pracownika
# 2 parametry obowiązkowe, i 2 opcjonalne
# ma zwrocic zmienną typu slownik

def utworz_pracownika(imie, nazwisko, email = "info@firma.pl", telefon = None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik

print (utworz_pracownika("Jan", "Kowalski")) # tylko parametry wymagane
print (utworz_pracownika("Adam", "Nowak", "adam@nowak.pl", "501234567")) # wszystkie parametry: wymagane i wszystkie opcjonalne
print (utworz_pracownika("Jan", "Zieliński", telefon="601602603"))
print (utworz_pracownika("John", "Rambo", "jan@zielinski")) # jeżeli numer parametru opcjonalnego pokrywa się z numerem parametru na liście parametrów funkcji, to nie musimy podawac nazy tego parametru
print (utworz_pracownika(email="bolek@agent.pl", nazwisko="Wałęsa", imie="Lech", telefon="999444555")) # jeżeli podajemy nazwy parametrow to możemy w dowolnej kolejnosci podawać parrametry obowiazkowe i opcjonalne

