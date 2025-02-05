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