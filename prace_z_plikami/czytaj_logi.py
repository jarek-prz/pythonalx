'''
otworz plik
czytaj logi

python czytaj_logi.py logs.txt

ile czasu sumarycznie kazdy uzytkownik byl zalogowany w systemie

cd C:\Users\kurs\PycharmProjects\test\prace_z_plikami
python czytaj_logi.py logs.txt
'''

import sys

#plik = sys.argv[1]
plik = "dane/logs.txt"
# 1 czytanie pliku

# lista logow plus_minus
def lista_logow_pm(plik):
    logi = []
    with open(plik, 'r') as f:
        for linia in f:
            dane_z_linii =linia.strip().split(';')
            logi.append(dane_z_linii)
    return logi

a= lista_logow_pm(plik)

def czasy(logi):
    czasy = {}
    for log in logi:
        user=log[0]

        # czas_przed
        if czasy.get(user) == None:
            liczba_sekund_przed = 0
        else:
            liczba_sekund_przed = czasy[user]

        # roznica z logu
        if log[1]=="LOGIN":
            sekundy_pm = -1 * int(log[2])
        elif log[1]=="LOGOUT":
            sekundy_pm =  int(log[2])

        # czasy po
        czasy[user]=liczba_sekund_przed+sekundy_pm

    sorted_x = sorted(czasy.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_x


for c in czasy(a):
    print(c)






