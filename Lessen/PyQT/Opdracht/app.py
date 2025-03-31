from PyQt6.core import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from feiten_eng import Facts
from feiten_nl import Feiten
from feiten_frans import Faits
from feiten_duits import Fakten

import random

feiten_eng = Facts
feiten_nl = Feiten
feiten_frans = Faits
feiten_duits = Fakten

class MijnScherm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("4 Knoppen, 4 Talen & 50 feitjes!")

        self.knop_engels = QPushButton()
        self.knop_engels.setText("Generate fact")
        self.knop_engels.clicked.connect(self.knop_ingedrukt)
        self.knop_engels.move(64,32)
        self.knop_engels.setFixedSize(200, 200)

        self.knop_duits = QPushButton()
        self.knop_duits.setText("Fakten erzeugen")
        self.knop_duits.clicked.connect(self.knop_ingedrukt)
        self.knop_duits.move(64,64)
        self.knop_duits.setFixedSize(200, 200)

        self.knop_frans = QPushButton()
        self.knop_frans.setText("Générer des faits")
        self.knop_frans.clicked.connect(self.knop_ingedrukt)
        self.knop_frans.move(128,32)
        self.knop_frans.setFixedSize(200, 200)

        self.knop_nederlands = QPushButton()
        self.knop_nederlands.setText("Genereer feit")
        self.knop_nederlands.clicked.connect(self.knop_ingedrukt)
        self.knop_nederlands.move(128,64)
        self.knop_nederlands.setFixedSize(200, 200)

        self.output_venster = QTextEdit(self)
        self.output_venster.move(250, 600)
        self.output_venster.setPlaceholderText("Output")

        self.exit_knop = QCloseEvent

        self.setFixedSize(500, 700)
        
        layout = QGridLayout()
        layout.addWidget(self.knop_engels, 1,0)
        layout.addWidget(self.knop_nederlands, 1, 1)
        layout.addWidget(self.knop_duits, 2, 0)
        layout.addWidget(self.knop_frans, 2, 1)
        layout.addWidget(self.output_venster, 3, 0, 1, 2)
        self.setLayout(layout)
    
    def knop_ingedrukt(self):
        knop_naam = self.sender().text()

        if knop_naam == "Generate fact":
            self.output_venster.setPlainText(random.choice(feiten_eng))
        elif knop_naam == 'Fakten erzeugen':
            self.output_venster.setPlainText(random.choice(feiten_duits))
        elif knop_naam == 'Générer des faits':
            self.output_venster.setPlainText(random.choice(feiten_frans))
        elif knop_naam == 'Genereer feit':
            self.output_venster.setPlainText(random.choice(feiten_nl))

app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()