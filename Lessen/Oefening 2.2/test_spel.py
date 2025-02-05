from spel import spel


spel1 = spel("Catan", 120)
spel2 = spel("Monopoly", 40, "Bordspel")

spel1.set_speelduur(-10)
print(spel1)
spel1.set_speelduur(60)
print(spel1)
spel1.set_speelduur(120)

spel1.set_categorie("Strategie")
print(spel1)
spel1.set_categorie("Dobbelspel")
print(spel1)

spel2.set_categorie("Strategie")
print(spel2)
