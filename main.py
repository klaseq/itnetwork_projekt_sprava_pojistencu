from pojistenec import Pojistenec
from seznam import Seznam

seznam = Seznam()

while True:
    seznam.menu()
    try:
        vyber = int(input("Zadej operaci: "))
        if vyber < 1 or vyber > 4:
            raise Exception("Bylo zvoleno spatne cislo")
    except Exception as e:
        print(e)
        print("Prosim vyber validni cislo z menu")

    if vyber == 4:
        print("Program byl ukoncen")
        break
    elif vyber == 1:
        seznam.pridat()
        tlacitko = input("data byla ulozena, pokracujte libovolnou klavesou...")
    elif vyber == 2:
        seznam.vypis_seznam()
        tlacitko = input("pokracujte libovolnou klavesou...")
    elif vyber == 3:
        seznam.vyhledat()