from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QFileDialog, QLineEdit
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction, QPixmap


# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    # Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = None
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(100, 100, 600, 400)
        self.move(60, 15)

        self.createMenu()
        self.createTabs()

    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

        self.actionChooseImg = QAction('Choose img', self)
        self.actionChooseImg.setShortcut('Ctrl+A')
        self.actionChooseImg.triggered.connect(self.getFile)
        self.fileMenu.addAction(self.actionChooseImg)

    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()

        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = self.createTab1()
        self.tab_2 = self.createTab2()
        self.tab_3 = QWidget()

        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Pierwsza zakładka")
        self.tabs.addTab(self.tab_2, "Druga zakładka")
        self.tabs.addTab(self.tab_3, "Trzecia zakładka")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)

    def getFile(self):
        self.fileName, selectedFilter = QFileDialog.getOpenFileName(self.tab_1, "Wybierz plik obrazu",
                                                                    "Początkowa nazwa pliku",
                                                                    "PNG (*.png)")

        # Jeżeli nazwa została zwrócona (użytkownik wybrał plik), wyświetlenie obrazu za pomocą QPixmap
        if self.fileName:
            label = QLabel(self.tab_1)
            pixmap = QPixmap(self.fileName)
            label.setPixmap(pixmap)

            self.tab_1.resize(pixmap.width(), pixmap.height())
            self.tab_1.show()
            label.show()

    def createTab1(self):
        resultWidget = QWidget()
        return resultWidget

    def createTab2(self):
        return QLineEdit()


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()

