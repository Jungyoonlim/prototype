from PyQt5 import QApplication, QMainWindow, QAction, QFileDialog, QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap
import sys 

class MainWindow(QMainWindow):
    def __init__(self, mesh):
        super().__init__()
        self.mesh = mesh
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('3D model to 2d Parameterization')
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()