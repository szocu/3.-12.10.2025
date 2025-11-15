print("hello world!")

def createCar(marka, model, rocznik): # podejscie proiceduralne
    return {"Marka" : marka, "model " : model, "rocznik " : rocznik} # tworzenie slownika

auto = createCar("Audi", "A4", 1999)

#


# OOP

class Samochod:
    def __init__(self, marka, model, rocznik):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik

    def przedstaw_sie(self):
        print(f"Jestem {self.marka} {self.model}.\nI jestem z {self.rocznik} roku")
    

auto1 = Samochod("Seat", "Ibiza", 1992)
# auto1.przedstaw_sie()


class Licznik: # klasa zmiany stanu obiektu
    def __init__(self):
        self.licznik = 0


    def up(self):
        self.licznik += 1

    def down(self):
        self.licznik -= 1

    def pokaz(self):
        print("Stan licznika: ", self.licznik)



licznik = Licznik()
for i in range(1, 10):
    licznik.up()

licznik.down()


licznik.pokaz()



class Student: #atrybut instancji vs atrybut klasy
    uczelnia = "TEB Edukacja" #atrybut klasy, wspolny dla wszystkich instancji

    def __init__(self, imie, nazwisko):
        self.imie = imie #atrybut obiektu - instancji
        self.nazwisko = nazwisko



a = Student("Ola", "Kot")
b = Student("Rafał", "Kotowski")
c = Student("Wacław", "Kotanski")
d = Student("Ryszard", "Kotecki")

print(a.uczelnia)
print(b.uczelnia)
print(f"Uczeń:  {a.imie} {a.nazwisko}")


class Konto:
    def __init__(self, saldo = 0):
        self.__saldo = saldo # __ = atrybut prywatny, hermetyzacja lub enkapsulacja danych

    def wplata(self, kwota):
        self.__saldo += kwota

    def getSaldo(self): # dostep do atr prywatnych przez funkcje z return
        return self.__saldo







class KontoPremium(Konto): # dziedczienie
    def bonus(self):
        self._Konto__saldo += 50 # _Konto -> odwolanie do elementu dziedziczenia


konto1 = KontoPremium()
konto1.bonus()
konto1.wplata(100)
print(f"Stan konta to: {konto1.getSaldo()} ")


print()

class Zwierze:
    def dzwiek(self):
        pass  # przekazanie dalej i tyle, ale to nie ma nic wspolnego z polimorfizmem

# polimorfizm - metody o tej samej nazwie ale dzialajace inaczej, wielopostaciowosc, nie trzeba ani pass ani klasy nadrzednej, to dziala niezaleznie od tego
class Pies(Zwierze):
    def dzwiek(self):
        print("Hau")

class Kot(Zwierze):
    def dzwiek(self):
        print("Miau")


for z in [Pies(), Kot()]:
    z.dzwiek()

print()
print()

