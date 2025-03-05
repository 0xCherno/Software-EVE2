from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MijnScherm(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Restaurant Lake Side Mania")
        knop = QPushButton("Bestellen")
        knop.setCheckable(True)
        knop.clicked.connect(self.knop_ingedrukt)

        self.setCentralWidget(knop)
        self.setFixedSize(500, 500)

    def knop_ingedrukt(self):
        print("Knop ingedrukt!")

app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()
