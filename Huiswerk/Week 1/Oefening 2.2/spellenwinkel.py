from spel import spel

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
    
    def geef_spelllen(self, categorie):
        for spel in self.spellen:
            if spel.get_categorie() == categorie:
                return categorie
            print(f"Geen spellen in de categorie {categorie} gevonden")
