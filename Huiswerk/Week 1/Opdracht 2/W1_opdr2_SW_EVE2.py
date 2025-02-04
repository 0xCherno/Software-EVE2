class boeken:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.uitgeleend = False

    def leen_uit(self):
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
