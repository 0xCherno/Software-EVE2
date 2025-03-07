# data.py
from recept import Recept
from ingredient import Ingredient
from stap import Stap

class Data:
    recepten = []

    Studenten_Pasta_Carbonara = Recept("Studenten Pasta Carbonara", "Een goedkope versie van pasta Carbonara voor studenten!")
    Anabolische_Kwark = Recept("Anabolische kwark", "Een grote bak kwark met 62 gram eiwit en <500 kcal!")
    Kip_Rijst_Brocoli = Recept("Kip Rijst en Broccoli", "Een gezonde maaltijd voor na het sporten")

    # Ingrediënten voor Studenten Pasta Carbonara
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Spaghetti", 75, "gram", 267))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Voorgesneden spekjes", 50, "gram", 108))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Ei dooiers", 2, "stuks", 110))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Zwarte peper", 1, "theelepel", 0))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Parmigiano Reggiano", 30, "gram", 120))
    Studenten_Pasta_Carbonara.ingredient_list[-1].set_plantaardig_alternatief(("Vega Kaas", 20, "gram", 120))

    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Kook de spaghetti volgens de aanwijzingen op de verpakking"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Bak de spekjes in een pan tot ze knapperig zijn"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Klop de ei dooiers los in een kom"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Meng de gekookte spaghetti met de spekjes en het vet in de pan"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Voeg de losgeklopte ei dooiers toe en roer goed door"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Breng op smaak met zwarte peper en geraspte Parmigiano Reggiano"))

    # Ingrediënten voor Anabolische Kwark
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Magere kwark", 500, "gram", 250))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Proteïne poeder vanille", 30, "gram", 112))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Banaan", 100, "gram", 110))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Ongebrande cashewnoten", 25, "gram", 168))
    Anabolische_Kwark.voeg_stap_toe(Stap("Mix de proteïne poeder en kwark tot een egale mix"))
    Anabolische_Kwark.voeg_stap_toe(Stap("Voeg de banaan en cashewnoten toe"))
    Anabolische_Kwark.voeg_stap_toe(Stap("Serveer en geniet"))

    # Ingrediënten voor Kip Rijst Broccoli
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Rijst", 75, "gram ongekookt", 248))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Kipfilet", 200, "gram", 220))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Groentemix", 300, "gram", 168))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Gyros kruiden", 2, "gram", 2))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Olijfolie", 5, "gram", 41))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Sriracha", 10, "gram", 13))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Marineer de kipfilet met de gyros kruiden"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Bak de kipfilet in olijfolie"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Verwarm de groentemix in de magnetron"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Bereid de rijst volgens de instructies"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Serveer met sriracha"))

    recepten.append(Studenten_Pasta_Carbonara)
    recepten.append(Anabolische_Kwark)
    recepten.append(Kip_Rijst_Brocoli)
