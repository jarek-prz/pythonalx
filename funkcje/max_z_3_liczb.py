# napisz f która zwroci max z 3 podanych liczb
# w celu rozwiazania mozna napisac wiecej, niz 1 funkcje
# f nie moze miec wiecej niz 1 if

def max_of_two(a,b):
    max= a
    if b>max:
        max=b
    return max

def max_of_three(a,b,c):
    wynik=max_of_two(max_of_two(a,b), c)
    return wynik

r = max_of_three(-8,-1,-17)
print(r)

def test_max_of_three():
    r=max_of_three(10,1,17)
    assert r==17

