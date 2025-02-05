from spel import spel, spellenwinkel

#Winkels
winkel = spellenwinkel("Speeleiland", 10)

#Assortiment
spel1 = spel("Catan", "strategie", 300)
spel2 = spel("Monopoly", "bordspel", 90)
spel3 = spel("Uno", "kaartspel", 30)
spel4 = spel("Wingspan", "strategie", 40)
spel5 = spel("Ganzenbord", "bordspel", 30)

winkel.voeg_spel_toe(spel1)
winkel.voeg_spel_toe(spel2)
winkel.voeg_spel_toe(spel3)
winkel.voeg_spel_toe(spel4)
winkel.voeg_spel_toe(spel5)

print(winkel.zoeken_spel("Ganzebord"))