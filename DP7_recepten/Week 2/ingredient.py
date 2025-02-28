class Ingredient:
    def __init__(self, naam : str, hoeveelheid : int, eenheid : str, kcal : int):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid
        self.kcal = kcal
        self.plantaardig_alternatief = []

    def get_kcal(self):
        return self.kcal
    
    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam} {self.kcal}"
    