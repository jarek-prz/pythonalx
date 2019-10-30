import random # losowanie
DEBUG=True

# losujemy poczatkowe polozenia
gracz_x =random.randint(1 ,10)
gracz_y =random.randint(1 ,10)
skarb_x =random.randint(1 ,10)
skarb_y =random.randint(1 ,10)

# Obliczam odleglosc po wylosowaniu
odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
print("Odległość Gracza od Skarbu: ", odleglosc_po_wylosowaniu)

#W zaleznosci od zmiennej DEBUG printuje informacje o położeniu skarbu i gracza
if DEBUG:
    print(f"Położenie Gracza (x={gracz_x}, y={gracz_y})")
    print(f"Położenie Skarbu (x={skarb_x}, y={skarb_y})")
    print(f"Minimalna liczba ruchów = {odleglosc_po_wylosowaniu}")

print ("""
Witaj,
Twoim zadaniem jest odnalazienie skarbu.
Poruszanie się:
w - Góra
s - Dół
a - Lewo
d - Prawo
Po każdym ruchu możesz otrzymać informację czy się zbliżasz czy oddalasz.
""")

print(f"Minimalna liczba ruchów wynosi {odleglosc_po_wylosowaniu}.")
print(f"Uwaga: Po wykonaniu {odleglosc_po_wylosowaniu*2} kroków skarb zmieni położenie i trzeba będzie szukać od nowa.")

liczba_ruchow = 0
odleglosc_przed_ruchem = odleglosc_po_wylosowaniu
while True:

    if DEBUG:
        print(f"Położenie Gracza (x={gracz_x}, y={gracz_y})")
        print(f"Położenie Skarbu (x={skarb_x}, y={skarb_y})")
        odleglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        print(f"Minimalna odleglość odleglosc {odleglosc}")

    odleglosc_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    # pytamy gracza o ruch
    ruch = input("Wpisz komendę asdw:   ")

    # zmieniamy pozycje gracza zgodnie z komendą
    if ruch=='a':
        gracz_x = gracz_x - 1
    elif ruch == 's':
        gracz_y = gracz_y - 1
    elif ruch == 'd':
        gracz_x = gracz_x + 1
    elif ruch == 'w':
        gracz_y = gracz_y + 1
    else:
        print("Trzymaj się reguł!")
        continue

    liczba_ruchow = liczba_ruchow+1
    if liczba_ruchow>odleglosc_po_wylosowaniu*2:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        print(f"Uwaga: wykonałeś {odleglosc_po_wylosowaniu * 2} kroków. Skarb zmienił położenie i trzeba szukać od nowa.")
        continue

    # sprawdzenie, czy wypadliśmy poza planszę
    if not(1<= gracz_x <=10 and 1<= gracz_y <=10):
        print("Wypadłeś poza planszę!")
        break

    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if odleglosc_po_ruchu ==0:
        print(f"Wygrałeś! Twoja liczba ruchów to {liczba_ruchow}.")
        print(f"Minimalna liczba ruchów wynosiła {odleglosc_po_wylosowaniu}.")
        break

    los = random.randint(1,5)
    if los==1: # pech, brak podpowiedzi
      print("Pech, brak podpowiedzi 1 na 5 razy")
    else:
            if odleglosc_po_ruchu>odleglosc_przed_ruchem:
                print("Zimno")
            elif odleglosc_po_ruchu<odleglosc_przed_ruchem:
                print("Cieplo")

    polozenie_gracza_xy = str(gracz_x) + str(gracz_y)
    polozenie_skarbu_xy = str(skarb_x) + str(skarb_y)
    print(polozenie_gracza_xy)
    for y in range(1,11):
        for x in range(1,11):
            aktualny_punkt = str(x) + str(y)
            if polozenie_gracza_xy==aktualny_punkt:
                print(f"G", end="")
            elif polozenie_skarbu_xy == aktualny_punkt:
                print(f"S", end="")
            else:
                print(f"_", end="")
        print()
    print()















