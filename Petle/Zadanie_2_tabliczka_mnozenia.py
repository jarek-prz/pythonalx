help(print)

for i in range(5):
    print(i, end="-")

for i in range(5):
    print(i, sep="-")

for i in range(5):
    print(f"{i:5}", end="")

print()
print()
print ("-"*100)
# naglowek
print("          ", end="")
for k in range(10):
    print(f"{k:5}", end="")
print()
print()
#wiersze
for w in range(10):
    print(f"{w:5}", end="")
    print("     ", end="")
    for k in range(10):
        print(f"{k*w:5}", end="")
    print()




