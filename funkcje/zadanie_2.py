


""" napisz funkcje zwracajaca zbior wszystkich znakow wystepujacych w zadanym napisie wiecej niz podana liczba razy np
np.
#>>> wiecej_niz("ala ma kota a kot ma ale", 3)

"""


def wiecej_niz(text : str, b : int) -> set:
    result = set()
    for s in set(text): # set(text) zamienia text na set co oznacza, że robi tylko niepowtarzajace sie znaki
        if text.count(s) > b:
            result.add(s)
    return result


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set() # nie {}

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaa bbb cc dddd", 2) == {"a", "b", "d", " "}

