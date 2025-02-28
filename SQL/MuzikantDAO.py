class MuzikantDAO:

    def get_alle_muzikanten_en_bands(self):
        self.connect()

        query = """ 
            SELECT m.naam, m.instrument, m.id, b.naam, b.id
            FROM muzikant m
            INNER JOIN muzikant_speelt_in_band mb 
            ON m.id = mb.muzikant_id
            INNER JOIN band b
            on mb.band_naam = b.naam
        """

        self.cursor.execute(query)
        resultaten = self.cursor.fetchall()

        muzikant_dict = {}
        boeken_dict = {}

        for rij in resultaten:
            muzikant_naam = rij['naam']
            if muzikant_naam not in muzikant_dict:
                muzikant = Muzikant(muzikant_naam, )