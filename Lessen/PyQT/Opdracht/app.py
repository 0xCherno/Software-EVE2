from PyQt6.QtCore import *
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

        self.knop_engels = QPushButton("Generate fact")
        self.knop_engels.clicked.connect(self.knop_ingedrukt)
        self.knop_engels.move(64,32)
        self.knop_engels.setFixedSize(200, 200)

        self.knop_duits = QPushButton("Fakten erzeugen")
        self.knop_duits.clicked.connect(self.knop_ingedrukt)
        self.knop_duits.move(64,64)
        self.knop_duits.setFixedSize(200, 200)

        self.knop_frans = QPushButton("Générer des faits")
        self.knop_frans.clicked.connect(self.knop_ingedrukt)
        self.knop_frans.move(128,32)
        self.knop_frans.setFixedSize(200, 200)

        self.knop_nederlands = QPushButton("Genereer feit")
        self.knop_nederlands.clicked.connect(self.knop_ingedrukt)
        self.knop_nederlands.move(128,64)
        self.knop_nederlands.setFixedSize(200, 200)

        self.output_venster = QTextEdit(self)
        self.output_venster.move(250, 600)
        # self.output_venster.setFixedSize(400, 200)
        self.output_venster.setPlaceholderText("Output")

        self.setFixedSize(500, 700)
        
        layout = QGridLayout()
        layout.addWidget(self.knop_engels, 1,0)
        layout.addWidget(self.knop_nederlands, 1, 1)
        layout.addWidget(self.knop_duits, 2, 0)
        layout.addWidget(self.knop_frans, 2, 1)
        layout.addWidget(self.output_venster, 3, 0, 1, 2)
        self.setLayout(layout)
    
    def knop_ingedrukt(self):
        self.sender()
        knop_naam = self.sender().text()

        if knop_naam == "Generate fact":
            print(f"{random.choice(feiten_eng)}\n")
        elif knop_naam == 'Fakten erzeugen':
            print(f"{random.choice(feiten_duits)}\n")
        elif knop_naam == 'Générer des faits':
            print(f"{random.choice(feiten_frans)}\n")
        elif knop_naam == 'Genereer feit':
            print(f"{random.choice(feiten_nl)}\n")
        else:
            print(f"Knop niet herkend {knop_naam}")
        return

app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()