import csv
import json

class MenadzerPlikow:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    
    def zapisz(self, dane):
        with open(self.nazwa, "w", encoding="utf-8") as plik: # as plik to alias; with open - z otwarcia 'w' - write
            plik.write(dane) # with automatycznie zamyka plik po zakonczeniu pracy

    def odczytaj(self):
        with open(self.nazwa, "r", encoding="utf-8") as plik: # 'r' - read
            for linia in plik:
                if linia != "":
                    print(linia) # to nie dziala
             
            return plik.read()
        



plik = MenadzerPlikow("notatka.txt")
# plik.zapisz("Witaj w Świecie Obiektów!")
print(plik.odczytaj())
    

#zapis csv

with open("dane.csv", "w", newline = "", encoding="utf-8") as plik:
    writer = csv.writer(plik)
    writer.writerow(["imię", "wiek"])
    writer.writerow(["Ania", 20])
    writer.writerow(["Tomasz", 40])

#odczyt csv

with open("dane.csv", "r", encoding="utf-8") as plik:
    reader = csv.reader(plik)
    for wiersz in reader:
        print(wiersz)



#zapis i odczyt json
osoba = {"imie" : "Kasia", "wiek" : 24,  "miasto" : "Bydgoszcz"}

#zapis
with open("osoba.json", "w", encoding="utf-8") as plik:
    json.dump(osoba, plik, ensure_ascii=False, indent=4)


#odczyt
with open("osoba.json", "r", encoding="utf-8") as plik:
    dane = json.load(plik)

print(dane)
print(dane["imie"])

