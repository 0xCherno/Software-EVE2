from recept import Recept
from ingredient import Ingredient
from stap import Stap

class Data:
    recepten = []

    Studenten_Pasta_Carbonara = Recept("Studenten Pasta Carbonara", "Een goedkope versie van pasta Carbonara voor studenten!")
    Anabolische_Kwark = Recept("Anabolische kwark", "Een grote bak kwark met 62gram eiwit en <500kcal!")
    Kip_Rijst_Brocoli = Recept("Kip Rijst en Brocoli", "Een gezonde maaltijd voor na het sporten")

    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Spaghetti", 75, "gram", "267 Kcal"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Voorgesneden spekjes", 50, "gram"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Ei dooiers", 2, "stuks"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Zwarte peper", 1, "Thee lepel(s)"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Paramgiano reggiano", 75, "gram"))
    

    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Kook de spaghetti volgens de aanwijzingen op de verpakking"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Bak de spekjes in een pan tot ze knapperig zijn"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Klop de ei dooiers los in een kom"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Meng de gekookte spaghetti met de spekjes en het vet in de pan"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Voeg de losgeklopte ei dooiers toe en roer goed door"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Breng op smaak met zwarte peper en geraspte Parmigiano Reggiano"))

    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Magere kwark", 500, "gram"))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Proteine poeder vanille", 30, "gram/ 1 scoop"))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Banaan", 100, "gram"))
    Anabolische_Kwark.voeg_ingredient_toe(Ingredient("Ongebrande cahsew noten", 25, "gram"))

    Anabolische_Kwark.voeg_stap_toe(Stap("Gooi de proteine poeder en kwark in een grote bak en mix totdat de kwark en proteine poeder 1 egale mix zijn"))
    Anabolische_Kwark.voeg_stap_toe(Stap("Voeg de banaan en cashew noten toe"))
    Anabolische_Kwark.voeg_stap_toe(Stap("Klaar!"))

    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Rijst", 75, "gram ongekookt"))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Kipfilet", 200, "gram"))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Groentemix", 300, "gram"))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Gyros kruiden", 2, "gram"))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Olijf olie", 5, "gram"))
    Kip_Rijst_Brocoli.voeg_ingredient_toe(Ingredient("Siracha", 10, "gram"))

    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Snij de kipfilet in stukjes en marineer met de gyros kruiden"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Bak de kipfilet goudbruin in een hete pan met 5 gram olijf olie"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Weeg 300 gram groentemix af en verwarm volgens de aanwijzigen in de magnetron"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Bereid 75 gram ongekookte rijst volgens de instructies"))
    Kip_Rijst_Brocoli.voeg_stap_toe(Stap("Serveer met siracha wanneer klaar!"))

    recepten.append(Studenten_Pasta_Carbonara)
    recepten.append(Anabolische_Kwark)
    recepten.append(Kip_Rijst_Brocoli)
