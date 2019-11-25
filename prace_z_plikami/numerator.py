'''
napisz funkcję, która otworz podany jako argument plik (podana nazwa pliku)
i wypisze o numerujac linie

pozwol na uruchomienie programu z konsoli commandline
python numerator.py nazwa.txt
'''
#plik='nazwa.txt'



import sys
try:
    plik = sys.argv[1]
    def numerowanie(plik):
        with open(plik, 'r', encoding='utf-8') as f:
            a = 1
            for l in f:
                print(f"{a}. {l.rstrip()}")
                a = a + 1
    numerowanie(plik)
except Exception:
    print("Wyjątek")