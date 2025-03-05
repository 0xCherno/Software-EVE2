from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from random import choice
from Lessen.PyQT.Opdracht.feiten_eng import Facts
from Lessen.PyQT.Opdracht.feiten_nl import Feiten
from Lessen.PyQT.Opdracht.feiten_frans import Faits
from Lessen.PyQT.Opdracht.feiten_duits import Fakten


feiten_eng = Facts
feiten_nl = Feiten
feiten_frans = Faits
feiten_duits = Fakten

class MijnScherm(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("4 Knoppen & 50 feitjes!")
        self.x_keren_ingedrukt = 0

        self.feit_engels = QPushButton("fact")
        self.feit_engels.clicked.connect(self.knop_is_ingedrukt)

        self.feit_duits = QPushButton("Tatsache")
        self.feit_duits.clicked.connect(self.knop_is_ingedrukt)

        self.feit_frans = QPushButton("fait")
        self.feit_frans.clicked.connect(self.knop_is_ingedrukt)

        self.feit_nederlands = QPushButton("feit")
        self.feit_nederlands.clicked.connect(self.knop_is_ingedrukt)

        self.setCentralWidget(self.)
        self.setFixedSize(500, 500)

    def knop_is_ingedrukt(self):
        print("Ingedrukt")
        nieuwe_scherm_titel = choice(scherm_titels)
        print(f"Nieuwe titel is: {nieuwe_scherm_titel}")
        self.setWindowTitle(nieuwe_scherm_titel)
    
    def scherm_titel_gewijzigd(self, scherm_titel):
        print(f"De titel van het scherm is gewijzigd: {scherm_titel}")

        if scherm_titel == 'error':
            self.knop.setDisabled(True)
            print("Error: something went wrong, button disabled")

app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()