import turtle
#print(help(turtle))

def rysuj_wielokat(liczba_katow):
    turtle.speed(1000)
    kat = 360/liczba_katow
    dlugosc = 1000/liczba_katow
    for i in range(liczba_katow):
        turtle.forward(dlugosc) # idzie do przodu o zadaną liczbę kroków
        turtle.right(kat) # skreca w prawo o zadany kąt
    turtle.done()

#rysuj_wielokat(5)

# zadanie szachownica

"""
    
    setheading(0) - east
    setheading(90) - north
    setheading(180) - west
    setheading(270) - south
    
"""


def rysuj_szachownice():
    turtle.speed(5000)

    # pole czarne
    for i in range(25):
        turtle.setheading(0) # - east
        turtle.forward(50)
        turtle.setheading(270) #- south
        turtle.forward(1)
        turtle.setheading(180)  # - west
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(1) #- south
    # powrot
    turtle.setheading(90) #- north
    turtle.forward(50)
    turtle.setheading(0)  # - east
    turtle.forward(50)

    # pole biale
    turtle.forward(50)
    turtle.setheading(270)  # - east
    turtle.forward(50)
    turtle.setheading(180)  # - west
    turtle.forward(50)
    turtle.setheading(90)  # - north
    turtle.forward(50)
    turtle.setheading(180)  # - east
    turtle.forward(50)

    turtle.done()

rysuj_szachownice()