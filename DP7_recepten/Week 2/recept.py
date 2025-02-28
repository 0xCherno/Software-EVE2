from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam : str, omschrijving : str,):
        self.naam = naam
        self.omschrijving = omschrijving
        self.ingredient_list = []
        self.stap_list = []
        self.aantal_personen = 1
    
    def voeg_ingredient_toe(self, ingredient):
        self.ingredient_list.append(ingredient)

    def get_ingredient(self):
        return self.ingredient_list
    
    def get_naam(self):
        return self.naam
    
    def get_omschrijving(self):
        return self.omschrijving
    
    def voeg_stap_toe(self, stap):
        self.stap_list.append(stap)

    def __str__(self):
        ingredienten_str = "\n".join(f"- {str(ing)}" for ing in self.ingredient_list)
        stappen_str = "\n".join(f"{i+1}. {str(stap)}" for i, stap in enumerate(self.stap_list))
        
        return (f"{self.naam}\n\n"
                f"{self.omschrijving}\n\n"
                f"Ingrediënten:\n{ingredienten_str}\n\n"
                f"Bereidingswijze:\n{stappen_str}\n")
    
    def set_aantal_personen(self, personen):
        self.aantal_personen = personen
    
    def get_aantal_personen(self):
        return self.aantal_personen
    
    def set_plantaardig_recept(self, plantaardig):
        self.plantaardig_recept.append(plantaardig)
    
    def get_plantaardig_recept(self):
        return self.plantaardig_recept

    