from recept import recept
from ingredient import Ingredient
from stap import Stap


def main():
    recepten = []

    Studenten_Pasta_Carbonara = recept("Studenten Pasta Carbonara", "Een goedkope versie van pasta Carbonara voor studenten!")
    Anabolische_Kwark = recept("Anabolische kwark", "Een grote bak kwark met 62gram eiwit en <500kcal!")
    Kip_Rijst_Brocoli = recept("Kip Rijst en Brocoli")


    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Spaghetti", 75, "gram"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Voorgesneden spekjes", 50, "gram"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Ei dooiers", 2, "stuks"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Zwarte peper", 2, "Thee lepels"))
    Studenten_Pasta_Carbonara.voeg_ingredient_toe(Ingredient("Paramgiano reggiano", 75, "gram"))

    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Kook de spaghetti volgens de aanwijzingen op de verpakking"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Bak de spekjes in een pan tot ze knapperig zijn"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Klop de ei dooiers los in een kom"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Meng de gekookte spaghetti met de spekjes en het vet in de pan"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Voeg de losgeklopte ei dooiers toe en roer goed door"))
    Studenten_Pasta_Carbonara.voeg_stap_toe(Stap("Breng op smaak met zwarte peper en geraspte Parmigiano Reggiano"))

    

    recepten.append(Studenten_Pasta_Carbonara, Anabolische_Kwark, Kip_Rijst_Brocoli)
    