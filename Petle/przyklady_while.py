
import random # losowanie
#print(dir(random))
#print(help(random.randint))
#print((random.randint(1,10)))  # łącznie z 1 i 10



#max(1,2,3) # max z liczb
#abs(-100) # wartosc bezwzględna

odleglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
print("Odległość Gracza od Skarbu: ", odleglosc)

#while (skarb_x!=gracz_x )

gracz_x=random.randint(1,10)
gracz_y=random.randint(1,10)
skarb_x=random.randint(1,10)
skarb_y=random.randint(1,10)

print ("Położenie Gracza: ", gracz_x, gracz_y)
print ("Położenie Skarbu: ", skarb_x, skarb_y)
while True:
    odleglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)



