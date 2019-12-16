'''
powtórka z obsługi plików
'''

'''
# musimy na koncu zrobić close
fd = open("dane.txt", "rt")
for index, linia in enumerate(fd, 1):
    print("krok ", index, ":", linia, end='')
fd.close()
'''

'''
https://api.um.warszawa.pl/#
http://api.nbp.pl/
'''


# context manager
with open("dane.txt", "rt") as fd:
    for index, linia in enumerate(fd, 1):
        print("krok ", index, ":", linia, end='')

print("\nCzy plik zamknięty:", fd.closed)
