class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid

    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam}"