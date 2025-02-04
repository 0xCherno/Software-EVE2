class boeken:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.uitgeleend = False

    def leen_uit(self):
        if self.uitgeleend == False:
            print("Helaas het boek is uitgeleend")
        else:
            self.uitgeleend = True
            print("Bedankt voor het lenen van het boek, veel lees plezier!")

        

    def breng_terug(self):
        if self.uitgeleend == True:
            print("Bedankt voor het terug brengen van het boek!")
            self.uitgeleend = False
        else:
            print(f"Fout Het boek {self.titel} is uitgeleend.")

    def __str__(self):
        return F"Titel {self.titel}, auteur {self.auteur}, jaar {self.jaar}, uitgeleend: {self.uitgeleend}"

