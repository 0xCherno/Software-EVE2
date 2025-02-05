class boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.uitgeleend = False

    def leen_uit(self):
<<<<<<< HEAD:Huiswerk/W1_opdr2_SW_EVE2.py
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
=======
        if self.uitgeleend == False:
            self.uitgeleend = True
            print(f"Bedankt voor het lenen van {self.titel}, veel lees plezier!")
        else:
            print(f"Fout Het boek {self.titel} is al uitgeleend.")

    def breng_terug(self):
        if self.uitgeleend == True:
            self.uitgeleend = False
            print("Bedankt voor het terug brengen van het boek!")
        else:
            print(f"Fout Het boek {self.titel} is niet uitgeleend.")

    def status(self):
        if self.uitgeleend == False:
            status = "Nee"
        else:
            status = "Ja"
        return status

    def __str__(self):
        return F"Titel {self.titel}, auteur {self.auteur}, jaar {self.jaar}, uitgeleend: {self.status()}"
>>>>>>> a9d431f4bd62e4f00ed930edeffcd8e5ec2c2cb0:Huiswerk/Week 1/Opdracht 2/W1_opdr2_SW_EVE2.py
