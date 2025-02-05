class huisdier:
    def __init__(self, naam, soort, leeftijd):
        self.naam = naam
        self.soort = soort
        self.leeftijd = leeftijd
        self.honger = False
        self.voedingsschema = []
    
    def voeg_maaltijd_toe(self):
        for i in range (0, 7):
            nieuwe_maaltijd = str(input(f"Geef maaltijden op voor {self.naam} van Ma/ Zondag: "))
            self.voedingsschema.append(nieuwe_maaltijd)
            i += 1
    
    def toon_voedingsschema(self):
        print(f"Voedingschema {self.naam} Ma/ Zondag: ",*self.voedingsschema, sep='\n- ')
    
    def voed(self):
        if self.honger == True:
            self.honger = False
            print(f"{self.naam} heeft eten gekregen en zit nu vol!")
        else:
            print(f"{self.naam} zit vol!")
    
    def maak_hongerig(self):
        self.honger = True
    
    def status_honger(self):
        if self.honger == False:
            status = "Nee"
        else:
            status = "Ja"
        return status

    def __str__(self):
        return f"Naam: {self.naam}, Soort: {self.soort}, Leeftijd: {self.leeftijd}, Hongerig: {self.status_honger()}"

    