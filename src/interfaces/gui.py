import sys 
import os 

# Absolute path to the directory of the current script (gui.py)
current_dir = '/Users/jungyoonlim/unwrap/src/interfaces'

# The 'src' directory is one level up from the 'interfaces' directory
src_dir = os.path.dirname(current_dir)

# Add the 'src' directory to sys.path to be able to import the TriangleMesh
sys.path.append(src_dir)

from mesh.barycentric.triangle import TriangleMesh
# Your other import statements and the rest of your code follow

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel,
                             QMainWindow, QFileDialog, QGraphicsScene, QGraphicsView,
                             QGraphicsEllipseItem, QStackedWidget)
from PyQt5.QtCore import Qt 

class SignInForm(QWidget):
    def __init__(self, main_window, parent=None):
        """
        Initialize the object with the provided mesh.

        Parameters:
            mesh (type): Description of the mesh parameter.

        Returns:
            None
        """
        super(SignInForm, self).__init__(parent)
        self.main_window = main_window 
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Enter username")
        layout.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Enter password")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        self.signInButton = QPushButton("Sign In", self)
        self.signInButton.clicked.connect(self.sign_in)
        layout.addWidget(self.signInButton)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        self.setLayout(layout)
    
    def sign_in(self):
        """
        Function to sign in with username and password.
        """
        username = self.username.text()
        password = self.password.text()
        if username == "admin" and password == "adminpw":
            self.main_window.switch_to_main_ui()
        else:
            self.error_label.setText("Invalid username or password")
            self.error_label.show()

class MainWindow(QMainWindow): 
    def __init__(self, mesh):
        super().__init__()
        self.mesh = mesh
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)
        self.initSignInUI()
        self.initMainUI()

    def initSignInUI(self):
        self.signInForm = SignInForm(main_window=self, parent=self) 
        self.stackedWidget.addWidget(self.signInForm)

    def initMainUI(self):
        # Placeholder for main UI setup
        # For example, create a widget to represent your main UI and add it to the stacked widget
        mainUI = QWidget()  # This should be replaced with actual UI setup
        self.stackedWidget.addWidget(mainUI)

    def switch_to_main_ui(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def display_uv_map(self):
        """
        Display the mesh with the parameterization.
        """
        if not hasattr(self.mesh, 'uvs'):
            print("UV coordinates are not calculated. Ensure a model is loaded and processed.")
            return 
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        for uv in self.mesh.uvs:
            scale = 100 
            offset = 300
            u, v = uv[0] * scale + offset, uv[1] * scale + offset
            ellipse = QGraphicsEllipseItem(u - 5, v - 5, 10, 10)
            ellipse.setBrush(Qt.blue)
            self.scene.addItem(ellipse)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
    
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
            self.mesh.calculate_uv_coordinates()
            self.display_uv_map()
        else: 
            print("No file selected.")


def main():
    app = QApplication(sys.argv)
    mesh = TriangleMesh()
    mainWindow = MainWindow(mesh)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


