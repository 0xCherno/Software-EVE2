class Ingredient:
    def __init__(self, naam : str, hoeveelheid : int, eenheid : str, kcal : int):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid
        self.kcal = int(kcal)
        self.plantaardig_alternatief = None

    def get_kcal(self):
        return self.kcal
    
    def set_hoeveelheid(self, hoeveelheid : float):
        self.hoeveelheid.append(hoeveelheid)

    def get_hoeveelheid(self):
        return self.hoeveelheid
    
    def set_plantaardig_alternatief(self, alternatief):
        self.plantaardig_alternatief = alternatief
    
    def get_ingredient(self, plantaardig : bool):
        if plantaardig == True:
            return self.plantaardig_alternatief
        else:
            return self

    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam} {self.kcal}"
