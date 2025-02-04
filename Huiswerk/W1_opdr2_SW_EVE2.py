class boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.uitgeleend = False

    def leen_uit(self):
        if self.uitgeleend == True:
            print("Helaas het boek is uitgeleend, probeer het later opnieuw!")
        else:
            print("Bedankt voor het lenen van het boek! Veel lees plezier")
            self.uitgeleend = True

    def breng_terug(self):
        if self.uitgeleend == False:
            print("Error, het boek is niet uitgeleend")
        else:
            print("Het boek is terug gebracht, dank je wel!")
            self.uitgeleend = False

    def __str__(self):
        return F"Titel {self.titel}, auteur {self.auteur}, jaar {self.jaar}, uitgeleend: {self.uitgeleend}"

boek1 = boek("Hobbit", "JRR Tolkien", 1973)

print(boek1)
boek1.leen_uit()
print(boek1)
boek1.leen_uit()
boek1.breng_terug()
print(boek1)
boek1.breng_terug()
