#list []
#tuple()
#dict{}
# dict
print(dict())

pol_ang = {
    #"klucz":"wartosc"
    "klucz":"key",
    "pies": "dog",
    "pies": "dog"
}

print(pol_ang)
print(pol_ang["pies"])


if "dog" in pol_ang:
    print(pol_ang["pies"])

print(pol_ang.get("dog")) # jeżeli klucza w slowniku n ie ma to dostajemy wartosc None

print(pol_ang.get("dog", "Brak takiergo hasla")) # jeżeli klucza w slowniku n ie ma to dostajemy wartosc "Brak takiergo hasla"
print(pol_ang.get("pies", "Brak takiergo hasla"))

# nowy klucz w slowniku
pol_ang["kot"]="cat"
print(pol_ang)

# kluczem moze byc int
pol_ang[1]="jeden"
print(pol_ang)

# tupla tez moze byc kluczem


print(pol_ang.keys()) # klucze (lista kluczy)
print(pol_ang.values()) # wartosci (lista wartosci)
print(pol_ang.items()) # klucz_wartosci (lista tupli)

# inne tworzeenie slownika
print(dict(krowa="cow", dom="house"))
# slownik tworzony z listy tupli
print(dict([("krowa","cow"), ("dom", "house")]))

#usuwanie ze slownika
print(pol_ang.pop("pies"))
print(pol_ang)

print(pol_ang.popitem())
print(pol_ang)

# set {} kolekcja unikalnych nieuporządkowanuych wartości
zbior = {1,2,3,4} # taki jakby slownuik, ale zlozony z samych wartosci
print(zbior, type(zbior))
print(dir(zbior))

zbior2= {1,"a", 2, "b", 3, "z"}
print(zbior2)

zbior2.add(9)
print(zbior2)

lista= [1,2,2,2,2,2,2,3,3,3,3,3,]
# po zrzutowaniu listy na set mamy zbior unikalnych wartosci
print(set(lista))

# operacje na setach podobne do operacji na zbiorach

# przy probie dodania nowego elelmnyu takiego jak ju zbyl to nie bedzie bledu, ale sie nie doda => musz a bytć unikalne
A = {1,2,3,4}
B = {3,4,5,6}
# suma zbiorow
print("suma zbiorow", A|B )
print("suma zbiorow", A.union(B) )

# roznica zbiorow
print("suma zbiorow", A-B )
print("suma zbiorow", A.difference(B) )

# częśc wspolna
print("suma zbiorow", A&B )
print("suma zbiorow", A.intersection(B) )

# roznica
print("suma zbiorow", A-B )
print("suma zbiorow", A.difference(B) )

# roznica symetryczna - suma zbiorów minus czesc wspolna
print("suma zbiorow", A ^ B )
print("suma zbiorow", A.symmetric_difference(B) )

# czy cos jest podzbiorem innego zbioru
C={1,2}
print("Czy jest podzbiorem:", C.issubset(A) )
