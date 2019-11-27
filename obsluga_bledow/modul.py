import random  # noqa:F401

# flake8
# python PEP8 - zbiór reguł pythona

lista = [1, 0, 10, 'a', 5555]

for i in lista:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Dzielenie przez zero")
    except TypeError:
        print("Dzielenie przez cos co nie jest liczba")
    except Exception:
        print("Inny błąd")
    finally:
        print("Zakończona iteracja")
