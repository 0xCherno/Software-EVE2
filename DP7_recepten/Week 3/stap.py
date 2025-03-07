class Stap:
    def __init__(self, beschrijving: str, tip=None):
        self.beschrijving = beschrijving
        self.tip = tip

    def __str__(self):
        if self.tip:
            return f"{self.beschrijving} (Tip: {self.tip})"
        return self.beschrijving
