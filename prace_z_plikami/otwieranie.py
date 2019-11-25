'''
stary sposob
f=open("test")
print(f)

# po linii
for line in f:
    print(line)

# od razu caly plik
print(f.read())
f.close()


'''





#print(2**7)


'''
try:
    f.open("test")
    # cos tu robimy
except Exception:
    print("Wyjątek")
finally:
    f.close()

'''

'''
manager kontekstu
'''

with open("test") as f:
    print(f.read())