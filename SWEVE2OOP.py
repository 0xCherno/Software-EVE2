class auto:
    def __init__(self, merk, uitvoering, bouwjaar, kleur, gewicht, max_snelheid, garantie, prijs):
        self.merk = merk
        self.uitvoering = uitvoering
        self.bouwjaar = bouwjaar
        self.kleur = kleur
        self.gewicht = gewicht
        self.max_snelheid = max_snelheid
        self.garantie = garantie
        self.rijbewijs_verplicht = "Ja"
        self.prijs = prijs
    
    def rijden(self, afstand, snelheid):
        self.rijden = True
        self.afstand = afstand
        self.snelheid = snelheid
        print(f"we rijden {afstand} kilometer naar onze bestemming met een snelheid van {snelheid}km/h")
    
    def lichten_aan(self, tijd):
        if tijd >= 19:
            print(f"En het is na {1900} in de avond, de lichten zijn aan")
        else:
            print("Het is nog niet donker, de lichten zijn uit")

auto1 = auto("bmw", "M2", 2020, "zwart", 1650, 230, 7, 68000)

print(auto1.merk, auto1.uitvoering, auto1.kleur)
auto1.rijden(120, 80)
auto1.lichten_aan(18)


# print(vars(auto1))

# auto1.merk = str(input("Geef de nieuwe merknaam op:"))
# auto1.uitvoering = str(input("Geef de uitvoering van de auto op:"))
# auto1.prijs = int(input("Geef de nieuwe prijs van de auto op:"))

# print(vars(auto1))

# print(f"de merknaam is gewijzigd naar {auto1.merk}, de uitvoering van de auto is {auto1.uitvoering} en de prijs is aangepast naar {auto1.prijs}.")