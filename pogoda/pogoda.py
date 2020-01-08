

"""

API: https://www.metaweather.com/api/
Id lokalizacji: https://www.metaweather.com/api/location/search/?query=london
Pogoda w lokalizacji: https://www.metaweather.com/api/location/44418/

osoba  = namedtuple("Osoba", ['imie'], ['wiek'])
os1 = osoba(imie='jarek', wiek=39)



Napisz program wyswietlajacy pogode dla wskazanej przez
uzytkownika lokalizacji.

Aplikacja ma działąć w trybie tekstowym:

Przykład użycia:
python pogoda.py warsaw

1. Skorzystaj z sys.argv
2. Obsłuż sytuację, gdy ktoś nie poda lokalizacji
3. Użyj namedtuple
4. Utwórz czytelne funckje - get_location_id, get_location_weather, report_weather
5. Zabezpiecz się przed wykonaniem kodu w momencie importu   (__name__  __main__


    the_temp = resp.json()[0]['the_temp']
    air_pressure = resp.json()[0]['air_pressure']
    humidity = resp.json()[0]['humidity']



"""
import sys
import requests
import json
from collections import namedtuple

weather = namedtuple("Weather", ['location_name','the_temp','air_pressure','humidity'])

url_id_lokalizacji="https://www.metaweather.com/api/location/search/?query="
url_pogoda_w_lokalizacji = "https://www.metaweather.com/api/location/"

def get_location_id():
    while True:
        try:
            location_name = (input("Podaj nazwę lokalizacji ")).lower()
            if len(location_name) >=3:
                resp = requests.get(url_id_lokalizacji + location_name)
                location_id = resp.json()[0]['woeid']
                break
        except Exception as exc:
            print("Błąd pobierania woeid dla podanego location_name", exc)
    return [location_name, location_id]

def get_location_weather(location):
    location_name=location[0]
    location_id = location[1]
    try:
        resp = requests.get(url_pogoda_w_lokalizacji + str(location_id))
        resp = resp.json()['consolidated_weather']
    except Exception as exc:
        print("Błąd pobierania pogody dla podanego id", exc)

    the_temp = resp[0]['the_temp']
    air_pressure = resp[0]['air_pressure']
    humidity = resp[0]['humidity']

    w = weather(location_name, the_temp, air_pressure, humidity)
    return (w)


location = get_location_id()
wea = get_location_weather(location)
print(wea)




