from pojistenec import Pojistenec
class Seznam:
    def __init__(self, pojistenci=None):
        self.pojistenci = pojistenci or []
        

    def pridat(self):
        while True:
            try:
                jmeno = input("Jmeno: ")
                prijmeni = input("Prijmeni: ")
                vek = int(input("Vek: "))
                cislo = int(input("Tel. cislo: "))
            except Exception as e:
                print(e)
                print("Chyba pri zadavani jmena nebo cisla pojistence, prosim zkuste znovu")
                continue
            break
        pojistenec = Pojistenec(jmeno, prijmeni, vek, cislo)
        self.pojistenci.append(pojistenec)

    def vyhledat(self):
        jmeno = input("Jmeno: ")
        prijmeni = input("Prijmeni: ")
        vyhledavani = [str(i) for i in self.pojistenci if (str(jmeno) and str(prijmeni)) in str(i)]
        if vyhledavani:
            print("\t-----------------------------------------------")
            for j in vyhledavani:
                print("\t",j)
            print("\t-----------------------------------------------")
        else:
            print("Nebyl nalezen zadny zaznam.")
    
    def menu(self):
        print("=========================\nEvidence pojistenych\n=========================")
        print("Vyber akci:")
        print("\t1 - pridat noveho pojistence")
        print("\t2 - vypsat vsechny pojistence")
        print("\t3 - vyhledat pojistence")
        print("\t4 - konec")

    def vypis_seznam(self):
        seznam = Seznam()
        print("seznam pojistenych:")
        print("\t-----------------------------------------------")
        for pojistenec in self.pojistenci:
            print("\t", pojistenec)
        print("\t-----------------------------------------------")