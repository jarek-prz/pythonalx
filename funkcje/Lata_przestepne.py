# wygeneruj liste lat przestepnych z zadanego okresu lat
# rok przestepny
# jest podzielna przez 4 ale nie przez 100
# lub jest podzielna przez 400

def czy_przestepny(rok):
    przestepny = False
    if (rok%400==0 or (rok%4==0 and rok%100!=0)):
        przestepny = True
    return przestepny

def lata_przestepne(rok_od, rok_do):
    if rok_od>rok_do:
        return None
    lata=list()
    for rok in range(rok_od, rok_do+1):
        if czy_przestepny(rok):
            lata.append(rok)
    return lata


print(lata_przestepne(2020,2030))


def test_lata_przestepne():
    assert (lata_przestepne(2020,2030) == [2020,2024, 2028]) is True




