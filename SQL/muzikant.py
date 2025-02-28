from band import band

class muzikant:

    def __init__(self, muzikant_id, naam, instrument):
        self.muzikant_id = muzikant_id
        self.naam = naam
        self.instrument = instrument
        self.bands_list = []
    
    def voeg_band_toe(self, band):
        self.bands_list.append(band)
    
    def __str__(self):
       return  (f"ID: {self.muzikant_id}\n"
                f"Naam: {self.naam}\n"
                f"Instrument(en): {self.instrument}\n"
                f"Band: {band.naam}\n")