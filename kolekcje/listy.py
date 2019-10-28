my_list = [1,"a", "Ala", "kot", 121]
print(my_list[2])

my_list_2 = [1,2,3, my_list]
print(my_list_2[3][2])

print(dir(my_list))

my_list.append(10)
print(my_list)

my_list.pop()
print(my_list)
print(my_list.pop()) # pop zwraca ostatni a wartosc z listy, ktra tez jednoczesnie kasuje
print(my_list.index("Ala")) # zwraca pozycję (index) pierwszego wystapienia podanej wartości
print(my_list.count("a")) # zwraca liczbę wystąpień danrgo obiektu w liście

a=[1,2,3]
b=[4,5,6]

print(a + b) # połączenie dwóch list
print(id(a), id(b))

a=b.copy()
a=b[:]

# podmiana element listy
a[0]=100
print(a)



# niemutowalna lista =  TUPLA
x=(1,2,3)  # np nie mozna podmienic, dodac ani usunąc elementu
print(dir(x)) # ma tylko metddy 'count', 'index'
# aler mozna dodaweac 2 tuple
y=(4,5,6)
z=x+y
print(z)

print(x.index(2))

# test czy coś zawiera się w liście albo tupli
print(100 in x) #  "False lub True"

# kluczem moze byc wszystko co jest hashowalne, czyli np lista nie moze byc ale tupla moze byc
#liczby, napisy, tuple,







