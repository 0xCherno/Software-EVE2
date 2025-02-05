class auto:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.eigenaar = "geen eigenaar"

    def verander_eigenaar(self):
        nieuwe_eigenaar = str(input("Geef de naam van de nieuwe eigenaar op: "))
        self.eigenaar = nieuwe_eigenaar
    
    def __str__(self):
        return f"Merk {self.merk}, Model: {self.model}, Bouwjaar: {self.bouwjaar}, eigenaar: {self.eigenaar}"


