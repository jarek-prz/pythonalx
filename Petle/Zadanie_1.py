# zapytaj użytkownika o 10 liczb i wypoisz ich średnią
#skorzystaj z petli for oraz funkcji range





# 2 wersja
print("Oblicza średnią z 10 pierwszych liczb")
suma=0
liczby_napis = input("Podaj 10 lub wiecej liczb rozdzielonych spacją")
liczby=liczby_napis.split(" ")
print(liczby)
for i in range(10):
    suma = suma + int(liczby[i])
print("Średnia = ", suma/10)


# 1 wersja
suma=0
for i in range(10):
   liczba =  input("Podaj liczbę:")
   suma = suma+int(liczba)
print("Średnia = ", suma/10)

print()