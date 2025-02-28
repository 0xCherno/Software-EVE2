CREATE TABLE muzikant(
	muzikant_id INT PRIMARY KEY,
    naam VARCHAR (80) NOT NULL,
    instrument VARCHAR (100) NOT NULL
    );
    
CREATE TABLE band(
	band_id INT PRIMARY KEY NOT NULL,
    naam VARCHAR (80)
);

CREATE TABLE muzikant_speelt_in_band(
	muzikant_id INT NOT NULL,
    band_id INT NOT NULL,
    PRIMARY KEY (muzikant_id, band_id),
    FOREIGN KEY (muzikant_id) references muzikant(muzikant_id),
    FOREIGN KEY (band_id) REFERENCES band(band_id)
);

INSERT INTO muzikant (muzikant_id, naam, instrument) VALUES
(1, 'Paul McCartney', 'Basgitaar, Zang'),
(2, 'John Lennon', 'Gitaar, Zang'),
(3, 'Linda McCartney', 'Keyboard, Zang');

INSERT INTO band (band_id, naam) VALUES
(1, 'Beatles'),
(2, 'Wings');

INSERT INTO muzikant_speelt_in_band (muzikant_id, band_id) VALUES
(1, 1),  
(1, 2),  
(2, 1),  
(3, 2);

select m.naam, b.naam
from muzikant m
inner join muzikant_speelt_in_band mb
on m.muzikant_id, = mb.band_id,
