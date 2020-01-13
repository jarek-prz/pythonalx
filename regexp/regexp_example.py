
'''
22 Sep 1994
[0-3][0-9]\s[A-Z][a-z]{2}\s[0-9]{4}
[0-3][0-9] \w{3}

przy ppomocy puythona zlaleźć wszystkie napisy z pliku input.txt

'''
import re

daty_pattern = "[0-3][0-9] \w{3} \d{4}"
kody_pocztowe_pattern = "\d{2}-\d{3}"
adresy_email_pattern = "[\w-.]+@[\w.]+"




with open("input.txt", 'r') as f:
    text = f.read()

daty_pattern=re.compile(daty_pattern)
daty = daty_pattern.findall(text)
print(daty)

kody_pocztowe_pattern=re.compile(kody_pocztowe_pattern)
kody = kody_pocztowe_pattern.findall(text)
print(kody)

#adresy_email_pattern=re.compile(adresy_email_pattern)
#email = adresy_email_pattern.findall(text)
#print(email)


text = "11 02 1980  11 15 1980"

dt_pattern = re.compile("((?:[0-2][1-9]|3[0-1]) (?:0[1-9]|10|11|12]) \d{4})")
print(dt_pattern.findall(text))

# napisać pattern który dopasuje liczbe dni do miesiaca
# np 11 Feb 2018 jest ok, ale 30 Feb 2018 nie jest ok
# to samo dla formatu 11 02 2018 oraz 30 02 2018


