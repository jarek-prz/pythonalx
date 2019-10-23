a=[1,2,3]

# if konczy działanie po napotkaniu pierwszego prawdziwego warunku
if 1 in a:
    print("1 jest w a")
elif 2+3==5:
    print("Matematyka działa")
elif 2 + 3 != 5:
    print("Matematyka nie działa")
else:
    print("1 nie ma w a")

print("Jestem poza wyrażeniem if")

x,y = 2,3  # z lewej i prawej jest jakby tupla i przyporządkowuje kolejno wartosci do zmiennych
print(x)

# operatory porównania
# ==, <, >, <=, >=, !=

# logiczne:
# and, or, not

#  okreslenie pozycji po x i y

x=95
y=95
s=""

if x<0 or x>100 or y<0 or y>100:
    s="Poza planszą"
elif x>=10 and x<=90 and y>=10 and y<=90:
    s = "W celu"
elif x<10:
    if y<10:
        s = "LDR"
    elif y<90:
        s = "LK"
    else:
        s = "LGR"
elif x < 90:
    if y < 10:
        s = "DK"
    elif y > 90:
        s = "GK"
elif x>90:
    if y<10:
        s = "PDR"
    elif y<90:
        s = "PK"
    else:
        s = "PGR"
print(s)


# sekwencja git:
# git status
# git add .
# git commit -m "Wszystko commit"
# git push origin master

