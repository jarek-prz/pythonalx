# napisac funkcje do obliczenioa pola i obwodu koła
# 1 tylko obwód
# 2. tylko pole
# 3 i to i to

from math import pi, sin
def oblicz_pole_kola(r):
    return pi * r**2

def oblicz_obwod_kola(r):
    return 2 * pi * r

def oblicz_pole_i_obwod_kola(r):
    p = oblicz_pole_kola(r)
    o = oblicz_obwod_kola(r)
    return p, o

print(oblicz_pole_i_obwod_kola(10))