#
# Oferujemy następujące produkty
# marchew:2.35, ziemniaki:2.20, cebula:1.70, ogórki:4
# Co chcesz kupić
# Ile chcesz kupic : marchew? 3
# Za marchew płacisz = 3*2,35 = 7,05

produkt_cena = {
    #"klucz":"wartosc"
    "marchew":2.35,
    "ziemniaki": 2.20,
    "cebula": 1.70,
    "ogórki":4,
    "melony":15.5
}

magazyn = {
    #"klucz":"wartosc"
    "marchew":20,
    "ziemniaki": 30,
    "cebula": 15,
    "ogórki":10,
    "melony":10
}

while True:
    print("="*100)
    tryb = input("Wybierz tryb: [z - zakupowy], [m - magazynowy] , [k - wyjście z programu] ")
    if tryb == "k":
        break
    if tryb=="m":
        while True:
            produkt = input("Jaki produkt chcesz dodać? ")
            magazyn["produkt"]=0
            ile = float(input("Ile kg produktu? "))
            stan = magazyn["produkt"]
            nowy_stan = stan + ile
            magazyn["produkt"] = nowy_stan
            print(f"Dodano {produkt}, {ile:.2f} kg. Stan poprzedni {stan:.2f} kg. Stan aktualny {magazyn['produkt']:.2f} kg. ")

            # obsługa nowego produktu
            if produkt_cena.get(produkt) == None:
                cena = float(input("Podaj cenę za 1 kg? "))
                produkt_cena["produkt"] = cena
            else:
                cena = produkt_cena[produkt]
            print(f"Dodano {ile:.2f} kg {produkt} po cenie {cena:.2f} zł/kg.")
            kolejny = input("Czy chcesz dodac kolejny produkt? [t/n] ? ")
            if kolejny=="n":
                break
    elif tryb== "z":
        while True:
            print("-" * 100)
            print("Oferujemy następujące produkty:")
            for i in produkt_cena:
                print(f"{i:10} - {produkt_cena[i]:.2f} zł/kg. Ilość w magazynie {magazyn[i]:.2f} kg")
            produkt = input("Co chcesz kupić? [wpisz 'k' aby zakończyć]")
            if produkt=="k":
                break
            cena_produktu = produkt_cena.get(produkt)
            if cena_produktu!=None:
                try:
                    ile = float(input(f"Ile kg {produkt} chcesz kupić? "))
                    stan_magazynu_produktu = magazyn[produkt]
                    # zmniejszenie stanu magazynu
                    while stan_magazynu_produktu-ile<0:
                        ile = float(input(f"Za mało produktu w magazynie ({stan_magazynu_produktu:.2f} kg). Podaj mniejszą ilość"))
                    magazyn[produkt]= stan_magazynu_produktu-ile
                    wartosc = ile * cena_produktu
                    print(f"Za {produkt} zapłacisz {wartosc:.2f} zł.")
                except KeyError:
                    print("Błąd systemu. Wykopki!")
            else:
                print("Nie ma takiego produktu")










