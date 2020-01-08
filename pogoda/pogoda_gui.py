import tkinter
import requests
import json
from collections import namedtuple

weather = namedtuple("Weather", ['location_name','the_temp','air_pressure','humidity'])
root = tkinter.Tk()

url_id_lokalizacji="https://www.metaweather.com/api/location/search/?query="
url_pogoda_w_lokalizacji = "https://www.metaweather.com/api/location/"

def get_location_id(location_name):
    while True:
        try:
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


def pokaz_pogode():
    location_name = location_name_entry.get()
    location=get_location_id(location_name)
    location_weather = get_location_weather(location)
    label_pogoda.configure(text=f"Temperatura: {location_weather.the_temp}")

label = tkinter.Label(master = root, text = "Podaj lokalizację ")
label.grid(row = 1, column = 1)

location_name_entry = tkinter.Entry(master = root)
location_name_entry.grid(row = 1, column = 2)

button = tkinter.Button(master=root, text="Pokaż pogodę", command=pokaz_pogode)
button.grid(row=2, column=1)

label_pogoda = tkinter.Label(master = root, text = "Pogoda: ")
label_pogoda.grid(row = 2, column = 2)


root.mainloop()




