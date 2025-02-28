class band:

    def __init__(self, band_id, naam):
        self.band_id = band_id
        self.naam = naam

    def __str__(self, band_id, naam):
        return f"{band_id}, {naam}"


