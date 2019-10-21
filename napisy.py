#
# Typ danych napisy (string)
#
napis1="Ala ma kota"
napis2='Ala ma kota'
napis3='A to jest "cudzysłów"'
napis4 = "A to jest \"cudzysłów\""
napis5 = "Znaki specjalne: \t, \n, \r, "
#print(napis4)
dlugosc = len(napis1)
#print("Dlugosc zmiennej napis 1 to: ", dlugosc, " znaków.")

#wiek = input("Podaj wiek")
#print("Twój wiek to ", wiek.strip())
s="Ruda tańczy jak Szalona"
# metody na rzecz zmiennesj string s
print(s.capitalize(), s.upper(), s.lower(), s.title(), s.swapcase())
print(s.center(100))
print(s.replace("R","D"))
print("Czy liczba? ", s.isdecimal())

h = "Hello!"
print(h[0])
print(h[-1])

print("Litera przedostatnia: ", s[-2])



