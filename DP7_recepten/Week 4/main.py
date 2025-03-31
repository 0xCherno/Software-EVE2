from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from recept import Recept
from ingredient import Ingredient
from stap import Stap
from data import Data

def genereer_pdf(recept, gebruik_plantaardig):
    pdf_bestandsnaam = recept.get_naam().replace(" ", "_") + ".pdf"
    pdf_canvas = canvas.Canvas(pdf_bestandsnaam, pagesize=A4)
    textobject = pdf_canvas.beginText(50, 800)
    textobject.setFont("Helvetica", 12)
    
    textobject.textLine("Recept: " + recept.get_naam())
    textobject.textLine("Omschrijving: " + recept.get_omschrijving())
    textobject.textLine("Aantal personen: " + str(recept.get_aantal_personen()))
    textobject.textLine("")
    textobject.textLine("Ingrediënten:")
    
    for ingredient in recept.ingredient_list:
        geselecteerd = ingredient.get_ingredient(gebruik_plantaardig)
        textobject.textLine(" - " + str(geselecteerd))
    
    textobject.textLine("")
    textobject.textLine("Bereidingswijze:")
    for index, stap in enumerate(recept.stap_list, start=1):
        textobject.textLine(str(index) + ". " + str(stap))
    
    pdf_canvas.drawText(textobject)
    pdf_canvas.showPage()
    pdf_canvas.save()
    print("PDF gegenereerd:", pdf_bestandsnaam)

def toon_recept_details(recept: Recept):
    try:
        aantal_personen = int(input("Geef het aantal personen op: "))
    except ValueError:
        print("Ongeldig aantal, standaard 1 persoon wordt gebruikt.")
        aantal_personen = 1
    recept.set_aantal_personen(aantal_personen)
    
    plantaardig_input = input("Wil je een plantaardig alternatief (ja/nee)? ").lower()
    gebruik_plantaardig = True if plantaardig_input == "ja" else False

    print("\n" + str(recept))
    print("Ingrediënten (met plantaardig alternatief indien gewenst):")
    for ingredient in recept.ingredient_list:
        geselecteerd = ingredient.get_ingredient(gebruik_plantaardig)
        print("- " + str(geselecteerd))

def voeg_recept_toe():
    print("\n=== Voeg een nieuw recept toe ===")
    recept_naam = input("Voer de naam van het recept in: ")
    recept_omschrijving = input("Voer de omschrijving van het recept in: ")
    nieuw_recept = Recept(recept_naam, recept_omschrijving)
    
    # Ingrediënten toevoegen
    while True:
        antwoord = input("Wil je een ingrediënt toevoegen? (ja/nee): ").lower()
        if antwoord != "ja":
            break
        ingredient_naam = input("Ingrediënt naam: ")
        try:
            ingredient_hoeveelheid = float(input("Hoeveelheid (voor 1 persoon): "))
        except ValueError:
            print("Ongeldige hoeveelheid, probeer opnieuw.")
            continue
        ingredient_eenheid = input("Eenheid: ")
        try:
            ingredient_kcal = float(input("Aantal kcal: "))
        except ValueError:
            print("Ongeldige kcal, probeer opnieuw.")
            continue
        nieuw_ingredient = Ingredient(ingredient_naam, ingredient_hoeveelheid, ingredient_eenheid, ingredient_kcal)
        
        alternatief_keuze = input("Heeft dit ingrediënt een plantaardig alternatief? (ja/nee): ").lower()
        if alternatief_keuze == "ja":
            alternatief_naam = input("Naam alternatief: ")
            try:
                alternatief_hoeveelheid = float(input("Hoeveelheid alternatief (voor 1 persoon): "))
            except ValueError:
                print("Ongeldige hoeveelheid voor alternatief, sla alternatief over.")
                alternatief_hoeveelheid = 0
            alternatief_eenheid = input("Eenheid alternatief: ")
            try:
                alternatief_kcal = float(input("Aantal kcal alternatief: "))
            except ValueError:
                print("Ongeldige kcal voor alternatief, sla alternatief over.")
                alternatief_kcal = 0
            if alternatief_hoeveelheid > 0:
                nieuw_ingredient.set_plantaardig_alternatief(
                    (alternatief_naam, alternatief_hoeveelheid, alternatief_eenheid, alternatief_kcal)
                )
        nieuw_recept.voeg_ingredient_toe(nieuw_ingredient)

    while True:
        antwoord = input("Wil je een bereidingsstap toevoegen? (ja/nee): ").lower()
        if antwoord != "ja":
            break
        stap_beschrijving = input("Voer de beschrijving van de stap in: ")
        tip = input("Optioneel: voeg een tip toe (of druk enter om over te slaan): ")
        if tip == "":
            tip = None
        nieuw_recept.voeg_stap_toe(Stap(stap_beschrijving, tip))
    return nieuw_recept

def verwijder_recept(recepten):
    recept_naam = input("Voer de naam van het recept dat je wilt verwijderen in: ")
    for rec in recepten:
        if rec.get_naam().lower() == recept_naam.lower():
            recepten.remove(rec)
            print("Recept '" + recept_naam + "' is verwijderd.")
            return
    print("Recept niet gevonden.")

def main():
    recepten = Data.recepten

    while True:
        print("\n=== Week 4 Menu ===")
        print("1. Toon recepten overzicht")
        print("2. Voeg recept toe")
        print("3. Verwijder recept")
        print("4. Genereer PDF voor recept")
        print("5. Afsluiten")
        
        keuze = input("Maak een keuze: ")
        if keuze == "1":
            if not recepten:
                print("Er zijn geen recepten beschikbaar.")
            else:
                for index, rec in enumerate(recepten, start=1):
                    print(f"{index}. {rec.get_naam()}")
                try:
                    selectie = int(input("Voer het nummer in van het recept dat je wilt bekijken: ")) - 1
                    if 0 <= selectie < len(recepten):
                        toon_recept_details(recepten[selectie])
                    else:
                        print("Ongeldige selectie.")
                except ValueError:
                    print("Voer een geldig nummer in.")
        elif keuze == "2":
            nieuw_recept = voeg_recept_toe()
            recepten.append(nieuw_recept)
            print("Recept toegevoegd.")
        elif keuze == "3":
            verwijder_recept(recepten)
        elif keuze == "4":
            try:
                selectie = int(input("Voer het nummer in van het recept voor PDF-generatie: ")) - 1
                if 0 <= selectie < len(recepten):
                    plantaardig_input = input("Gebruik plantaardig alternatief? (ja/nee): ").lower()
                    gebruik_plantaardig = True if plantaardig_input == "ja" else False
                    genereer_pdf(recepten[selectie], gebruik_plantaardig)
                else:
                    print("Ongeldige selectie.")
            except ValueError:
                print("Voer een geldig nummer in.")
        elif keuze == "5":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
if __name__ == "__main__":
    main()
