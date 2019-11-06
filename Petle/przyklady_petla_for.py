napis = "Ala ma kota" # napis
elementy = (1,'a', 2, 'c') # tupla
lista = [4,12,11,1] # lista
slownik = {1:"a", "Ala":"Kot", "Albert":"Einstein"} # slownik
zbior = {1,2,3,4,5} # set

for znak in napis:
    znak= znak.upper()
    print(znak)

# w pythonie zmienna w petli jest widoczna tez poza petlą - jako ostatnia wartosc
print("Ostatnia wartość ZNAK:",  znak)

for k in slownik.items():
    print(k)

# przerywanie pętli\

liczby = [1,2,3,10,20,30,100,200,300]

for liczba in liczby:
    if liczba>100000:
        break
    print(liczba)
else:
    print("petla wykonala się w calosci")

# range
print(range(10))
print(list(range(10)))
print(set(range(10)))
print(tuple(range(10)))

print(range(10,20,1))