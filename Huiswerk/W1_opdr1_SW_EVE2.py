class student:
    def __init__(self, naam, studentnummer, leeftijd):
        self.naam = naam
        self.studentnummer = studentnummer
        self.leeftijd = leeftijd

    def voeg_leeftijd_toe(self):
        self.leeftijd += 1
    
    def __str__(self):
        return f"Student naam: {self.naam}, Studentnummer: {self.studentnummer} en leeftijd: {self.leeftijd}"

#studenten
Student1 = student("Benjahmin Hekkers", 1216563, 21)

#output
Student1.voeg_leeftijd_toe()
print(Student1)

