from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from random import choice

scherm_titels = [
    'LSM',
    'Lake Side Mania',
    'Nog steeds LSM',
    'error',
]

class MijnScherm(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Restaurant Lake Side Mania")
        self.x_keren_ingedrukt = 0

        self.knop = QPushButton("Press me!")
        self.knop.clicked.connect(self.knop_is_ingedrukt)

        self.windowTitleChanged.connect(self.scherm_titel_gewijzigd)
        self.setCentralWidget(self.knop)
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
