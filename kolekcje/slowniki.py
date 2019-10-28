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
