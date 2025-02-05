class spel:
    def __init__(self, naam, speelduur, categorie = "???"):
        self.naam = naam
        self.__speelduur = speelduur
        self.categorie = categorie
    
    def __str__(self):
       return f"{self.naam} ({self.categorie}, {self.__speelduur})"

    def set_speelduur(self, speelduur):
        if speelduur < 0:
            print("Speelduur mag niet onder 0 komen.")
        else:
            self.__speelduur = speelduur
    
    def get_speelduur(self):
        return self.__speelduur
    
    def get_naam(self):
        return self.naam
    
    def set_categorie(self, categorie):
        if self.categorie == "???":
            self.categorie = categorie
        else:
            print("Categorie mag niet gewijzigd worden!")
            
    def get_categorie(self):
        return self.categorie

class spellenwinkel:
    def __init__(self, naam, capaciteit):
        self.naam = naam
        self.capaciteit = capaciteit
        self.spellen = []

    def voeg_spel_toe(self, spel):
        if len(self.spellen) < self.capaciteit:
            self.spellen.append(spel)
        else:
            print(f"De winkel {self.naam} heeft de maximale capaciteit bereikt")
    
    def __str__(self):
        spellen_info = f"---- {self.naam} ---- \n"
        for spel in self.spellen:
            spellen_info += f"{spel} \n"
        return spellen_info
    
    def geef_langste_spel(self):
        return max(self.spellen, key=lambda spel: spel.get_speelduur())

    def zoeken_spel(self, naam):
        for spel in self.spellen:
            if spel.get_naam() == naam:
                return naam
        print(f"Het spel {naam} is niet gevonden")
        return None
            
