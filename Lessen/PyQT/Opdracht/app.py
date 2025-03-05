from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from random import choice

#Importeren van de lijsten
from feiten_eng import Facts
from feiten_nl import Feiten
from feiten_frans import Faits
from feiten_duits import Fakten


feiten_eng = Facts
feiten_nl = Feiten
feiten_frans = Faits
feiten_duits = Fakten

class MijnScherm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("4 Knoppen & 50 feitjes!")
        self.x_keren_ingedrukt = 0

        self.knop_engels = QPushButton("Generate fact")
        self.knop_engels.clicked.connect(self.knop_ingedrukt)
        self.knop_engels.move(64,32)
        self.knop_engels.setFixedSize(200, 200)

        self.knop_duits = QPushButton("Fakten erzeugen")
        self.knop_duits.clicked.connect(self.knop_ingedrukt)
        self.knop_duits.move(64,64)
        self.knop_duits.setFixedSize(200, 200)

        self.knop_frans = QPushButton("générer des faits")
        self.knop_frans.clicked.connect(self.knop_ingedrukt)
        self.knop_frans.move(128,32)
        self.knop_frans.setFixedSize(200, 200)

        self.knop_nederlands = QPushButton("genereer feit")
        self.knop_nederlands.clicked.connect(self.knop_ingedrukt)
        self.knop_nederlands.move(128,64)
        self.knop_nederlands.setFixedSize(200, 200)

        self.setFixedSize(500, 700)
        
        layout = QGridLayout()
        layout.addWidget(self.knop_engels, 2,0)
        layout.addWidget(self.knop_nederlands, 2, 1)
        layout.addWidget(self.knop_duits, 3, 0)
        layout.addWidget(self.knop_frans, 3, 1)
        self.setLayout(layout)
    
    def knop_ingedrukt(self):
        print("Ingedrukt")


app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()