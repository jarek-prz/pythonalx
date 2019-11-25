
import sys
import re
import os

try:
    plik_dane = sys.argv[1]
except:
    plik_dane = "dane/emails.txt"

try:
    plik_wyniki = sys.argv[2]
except:
    plik_wyniki = "wyniki/emails_wyniki.txt"

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def wczytaj_i_wyczysc_emaile(plik):
    emails = []
    with open(plik, 'r', encoding='utf-8') as f:
        for email in f:
            if (re.search(regex, email)):
                emails.append(email.strip().upper())
    emails.sort()
    s = set(emails)
    return s

def zapisz_emaile(plik, s):
    with open(plik, "w") as f:
        for e in s:
            f.write(e + '\n')

zapisz_emaile(plik_wyniki, wczytaj_i_wyczysc_emaile(plik_dane))

# cd C:\Users\kurs\PycharmProjects\test\prace_z_plikami
# python czysc.py "dane/emails.txt" "wyniki/emails_wyniki.txt"

#file.read().splitlines()