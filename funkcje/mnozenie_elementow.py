'''
a - napisz funkcję, ktora wymnozy przez siebie elementy z listy wejsciowej
b - wybierze i zwroci z podanego napisu liste liczb np "a1b2c3d4" to w wyniku bedzie [1,2,3,4]
c  -  wersja b ale z liczbami, a nie cyframi

'''
# a
def pomnoz(lista):
    w=1
    for i in lista:
        w=w*i
    return  w

a= pomnoz([2,2,2,2,2])
print(a)

# b
def cyfry(napis):
    w=[]
    cyfry=["0","1","2","3","4","5","6","7","8","9",]
    for znak in napis:
        if znak in cyfry:
            w.append(int(znak))
    return w

a= cyfry("a1b2c3d4")
print(a)


#c
def liczby(napis):
    w=[]
    cyfry=["0","1","2","3","4","5","6","7","8","9"]
    next=False
    for znak in napis:
        if znak in cyfry:
            w.append(int(znak))
            next=True
            while next==True:
                a=1 # dokończyć w domu
    return w

a= cyfry("a100b201c304d40")
print(a)