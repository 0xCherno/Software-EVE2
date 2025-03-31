# main.py
from recept import Recept
from ingredient import Ingredient
from stap import Stap
from data import Data

def main():
    recepten = Data.recepten  # Lijst met recepten uit data.py

    while True:
        print("\nBeschikbare recepten:")
        for i, recept in enumerate(recepten, start=1):
            print(f"{i}. {recept.get_naam()}")

        keuze = input("\nVoer het nummer in van het recept dat je wilt bekijken (of 'q' om af te sluiten): ")
        if keuze.lower() == "q":
            print("Programma afgesloten.")
            break
        try:
            keuze_index = int(keuze) - 1
            if 0 <= keuze_index < len(recepten):
                geselecteerd_recept = recepten[keuze_index]
                try:
                    aantal = int(input("Geef het aantal personen op: "))
                except ValueError:
                    print("Ongeldig aantal, standaard 1 persoon wordt gebruikt.")
                    aantal = 1
                geselecteerd_recept.set_aantal_personen(aantal)

                plantaardig_input = input("Wil je een plantaardig alternatief (ja/nee)? ").strip().lower()
                plantaardig = True if plantaardig_input == "ja" else False
                
                print("\n" + str(geselecteerd_recept))
                print("Ingrediënten (met plantaardig alternatief indien gewenst):")
                for ingredient in geselecteerd_recept.ingredient_list:
                    ing = ingredient.get_ingredient(plantaardig)
                    print(f"- {ing}")
            else:
                print("Ongeldige invoer, kies een nummer uit de lijst.")
        except ValueError:
            print("Voer een geldig nummer in.")

if __name__ == "__main__":
    main()
