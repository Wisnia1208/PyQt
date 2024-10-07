from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QFileDialog, QLineEdit, QVBoxLayout, QSpinBox
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction, QPixmap


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

        # Dodanie opcji do wyboru obrazu
        self.actionChooseImg = QAction('Choose img', self)
        self.actionChooseImg.setShortcut('Ctrl+A')
        self.actionChooseImg.triggered.connect(self.getFile)
        self.fileMenu.addAction(self.actionChooseImg)

    # Funkcja dodająca widżety do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()

        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = self.createTab1()
        self.tab_2 = self.createTab2()
        self.tab_3 = self.createTab3()

        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Pierwsza zakładka")
        self.tabs.addTab(self.tab_2, "Druga zakładka")
        self.tabs.addTab(self.tab_3, "Trzecia zakładka")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)

    # Funkcja wyboru pliku i wyświetlenia obrazu
    def getFile(self):
        # Otwórz dialog wyboru pliku tylko dla plików PNG i JPG
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik obrazu",
                                                       "", "Obrazy (*.png *.jpg *.jpeg)")

        # Jeżeli plik został wybrany, wyświetl go
        if self.fileName:
            pixmap = QPixmap(self.fileName)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setScaledContents(True)  # Dopasowanie obrazu do rozmiaru QLabel
            self.imageLabel.resize(pixmap.width(), pixmap.height())
            self.tab_1.layout().update()  # Zaktualizowanie układu

    # Funkcja tworząca zakładkę 1 z możliwością wyświetlania obrazu
    def createTab1(self):
        resultWidget = QWidget()
        layout = QVBoxLayout()

        # Tworzymy QLabel do wyświetlania obrazu
        self.imageLabel = QLabel(resultWidget)
        layout.addWidget(self.imageLabel)

        resultWidget.setLayout(layout)
        return resultWidget

    # Zakładka 2 - Pole tekstowe
    def createTab2(self):
        return QLineEdit()

    # Zakładka 3 - Tworzenie pól A, B, C i wyniku
    def createTab3(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Pole A - Pole tekstowe
        self.textA = QLineEdit()
        self.textA.setPlaceholderText("Pole A")
        layout.addWidget(self.textA)

        # Pole B - Pole tekstowe
        self.textB = QLineEdit()
        self.textB.setPlaceholderText("Pole B")
        layout.addWidget(self.textB)

        # Pole C - Pole numeryczne
        self.numC = QSpinBox()
        self.numC.setRange(-1000, 1000)  # Ustawienie zakresu wartości od -1000 do 1000
        layout.addWidget(self.numC)

        # Pole wynikowe A + B + C
        self.resultField = QLineEdit()
        self.resultField.setReadOnly(True)  # Tylko do odczytu
        layout.addWidget(self.resultField)

        # Połączenie sygnałów zmian w polach A, B, C z funkcją updateResult
        self.textA.textChanged.connect(self.updateResult)
        self.textB.textChanged.connect(self.updateResult)
        self.numC.valueChanged.connect(self.updateResult)

        tab.setLayout(layout)
        return tab

    # Funkcja aktualizująca wynik w polu wynikowym
    def updateResult(self):
        # Pobranie wartości z pól A, B, C
        a = self.textA.text()
        b = self.textB.text()
        c = str(self.numC.value())

        # Sklejenie wartości A + B + C
        result = a + b + c

        # Ustawienie wyniku w polu wynikowym
        self.resultField.setText(result)


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()
