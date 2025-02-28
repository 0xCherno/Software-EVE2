from recept import Recept
from ingredient import Ingredient
from stap import Stap
from data import Data

def main():

    recepten = Data.recepten  #Lijst met ingredienten, recepten, etc staat in het bestandje data.py

    while True:
        print("\n Beschikbare recepten:")
        for i, recept in enumerate(recepten, start=1):
            print(f"{i}. {recept.get_naam()}")
    
        keuze = input("\nVoer het nummer in van het recept dat je wilt bekijken (Of q om het programma af te sluiten):")

        if keuze.lower() == "q":
            print("Programma afgesloten")
            break
        try:
            keuze_index = int(keuze) - 1
            if 0 <= keuze_index < len(recepten):
                recept = recepten[keuze_index]
                aantal_personen = Recept.set_aantal_personen(recept, (int(input("Geef het aantal personen op: "))))
                plantaardig = Ingredient.get_ingredient(recept, str(input("Wil je een plantaardig alternatief? Ja/Nee: ").lower))
                if plantaardig == "ja":
                    print("done")

                for i in range(aantal_personen):
                    print("success\n")
                

                    
                    


                







                # print("\n" + str(recepten[keuze_index]))
            else:
                print("Ongeldige invoer, kies een nummer uit de lijst.")
        except ValueError:
            print("Voer een geldig nummer in.")
        
if __name__ == "__main__":
    main()