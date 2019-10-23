#
# Array slicing
#


# slice'ing [X:Y]  X-początkowy indeks, Y: końcowy indeks, ale prawostronnie otwarty, czyli bez Y <X:Y)
h = "Hello!"
print(h[0:5])

# trzeci znak od końca
print(h[-3:-1])

s="Ruda tańczy jak szalona"
# parsowanie, np podział napisu np wg spacji
arr = s.split(" ")
print(arr)
print(arr[1])

# od 1 do 4 elementu listy, ale co drugi
print(s[0:15:2])

# cały string co 3 znak
print(s[0::3])
print(s[::3])

# reverse string w pythonie
print(s[::-1])

# Łączenie napisów
print("Hello " + "World")
a="Hello"
b="ALX"
print(f"{a} {b}")
