from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MijnScherm(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.knop_is_checked = False
        self.setWindowTitle("Restaurant Lake Side Mania")

        self.knop = QPushButton("Press me!")
        self.knop.setCheckable(True)
        self.knop.released.connect(self.knop_is_los)
        self.knop.setChecked(self.knop_is_checked)

        self.setCentralWidget(self.knop)
        self.setFixedSize(500, 500)

    def knop_is_los(self):
        self.knop_is_checked = self.knop.isChecked()
        print(self.knop_is_checked)

app = QApplication([])
scherm = MijnScherm()
scherm.show()
app.exec()
