# Pobierz tekst od użytkownika, zapytaj o szerokość, wyświetl tekst, który bedzie miał same duże litery
# tekst wycentrowany zgodnie z wartoscia szerokości


text = input("Podaj tekst ")
szerokosc = int(input("Podaj szerokosc "))

s=f"!{text.upper().center(szerokosc)}!"

print(s)






