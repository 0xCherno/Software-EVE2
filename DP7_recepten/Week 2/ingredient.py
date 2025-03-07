# ingredient.py
class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal: float):
        self.naam = naam
        self.basis_hoeveelheid = hoeveelheid
        self.hoeveelheid = hoeveelheid       
        self.eenheid = eenheid
        self.basis_kcal = kcal             
        self.kcal = kcal                    
        self.plantaardig_alternatief = None 

    def scale(self, aantal_personen: int):
        "Update de hoeveelheid en kcal op basis van het aantal personen."
        self.hoeveelheid = self.basis_hoeveelheid * aantal_personen
        self.kcal = self.basis_kcal * aantal_personen

    def set_plantaardig_alternatief(self, alternatief_data):
        "Stel een plantaardig alternatief in: (naam, hoeveelheid, eenheid, kcal)"
        self.plantaardig_alternatief = Ingredient(*alternatief_data)

    def get_ingredient(self, plantaardig: bool):
        "Haal het plantaardige alternatief op als dit gewenst is en bestaat."
        if plantaardig and self.plantaardig_alternatief is not None:
            return self.plantaardig_alternatief
        return self

    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam} ({self.kcal} kcal)"
