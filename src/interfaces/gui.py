import sys 
import os 
# sys.path.append('src/mesh/barycentric/triangle.py')
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel
from src.mesh.barycentric.triangle import TriangleMesh

class MainWindow(QMainWindow):
    def __init__(self, mesh):
        """
        Initialize the object with the provided mesh.

        Parameters:
            mesh (type): Description of the mesh parameter.

        Returns:
            None
        """
        super().__init__()
        self.mesh = mesh
        self.initUI()
    
    def initUI(self):
        """Initialize the UI window with title and size"""
        self.setWindowTitle('3D model to 2d Parameterization')
        self.setGeometry(100, 100, 800, 600)

        # Create and setup the file menu in the menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        # Create and setup the load action in the file menu
        loadAction = QAction('Load', self)
        loadAction.triggered.connect(self.loadModel)
        fileMenu.addAction(loadAction)
        
        # Create and setup the save action in the file menu
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.save)
        fileMenu.addAction(saveAction)

        # Create and setup the label for the window
        self.label = QLabel(self)
        self.label.move(10, 10)
        self.label.resize(780, 580)  # Slightly smaller to ensure it fits within the window
        self.label.setText("Load a 3D model to view its 2D parameterization.")  # Example text
        self.show()
    
    def save(self):
        """
        Save the mesh to a file dialog.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);;OBJ Files (*.obj)", options=options)
        if fileName:
            self.mesh.save_to_obj(fileName)
    
    def loadModel(self):
        """
        Load a model from a file dialog and load it into the mesh.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;OBJ Files (*.obj)", options=options)
        if fileName:
            self.mesh.load_from_obj(fileName)


def main():
    app = QApplication(sys.argv)
    mesh = TriangleMesh()
    mainWindow = MainWindow(mesh)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


