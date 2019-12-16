'''
pobieranie kursow walut via json
http://api.nbp.pl/api/exchangerates/tables/A/?format=json

ocean bibliotek
https://pypi.org/
'''
import requests
import json

url="http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
r = requests.get(url)
#print(r.text)

json_data=json.loads(r.text)
#print(type(json_data[0]))

nbp_data=json_data[0]
print(nbp_data.keys())

print(f"Tablica {nbp_data.get('table')} ")
print(f"Tablica {nbp_data.get('no')} ")
print(f"Tablica {nbp_data.get('effectiveDate')} ")

rates = nbp_data.get('rates')

for rate in rates:
    print("-"*60)
    print(f"{rate.get('currency')}\t\t{rate.get('code')}\t\t{rate.get('mid')}")

