from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QFileDialog, QLineEdit, QVBoxLayout, QSpinBox, \
    QPushButton, QTextEdit
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction, QPixmap


# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow
class Window(QMainWindow):
    # Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileName = None
        self.fileNameG = None
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



        self.task1menu = self.menu.addMenu("Task1")
        self.actionChooseImg = QAction('Open', self)
        self.actionChooseImg.setShortcut('Ctrl+A')
        self.actionChooseImg.triggered.connect(self.getFile)
        self.task1menu.addAction(self.actionChooseImg)

        self.task2menu = self.menu.addMenu("Task2")

        self.actionClearTxt = QAction('Clear', self)
        self.actionClearTxt.triggered.connect(self.clearText)
        self.actionClearTxt.setShortcut('Ctrl+1')

        self.actionOpenTxt = QAction('Open', self)
        self.actionOpenTxt.triggered.connect(self.openFile)
        self.actionOpenTxt.setShortcut('Ctrl+2')

        self.actionSaveTxt = QAction('Save', self)
        self.actionSaveTxt.triggered.connect(self.saveFileSame)
        self.actionSaveTxt.setShortcut('Ctrl+3')

        self.actionSaveAsTxt = QAction('Save as', self)
        self.actionSaveAsTxt.triggered.connect(self.saveFile)
        self.actionSaveAsTxt.setShortcut('Ctrl+4')

        self.task2menu.addAction(self.actionClearTxt)
        self.task2menu.addAction(self.actionOpenTxt)
        self.task2menu.addAction(self.actionSaveTxt)
        self.task2menu.addAction(self.actionSaveAsTxt)

        self.task3menu = self.menu.addMenu("Task3")
        self.actionClearTask3 = QAction('Clear', self)
        self.actionClearTask3.triggered.connect(self.clearAll3)
        self.actionClearTask3.setShortcut('Ctrl+5')
        self.task3menu.addAction(self.actionClearTask3)

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


    # Zakładka 2 - Prostota notatnika
    def createTab2(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Pole tekstowe do wyświetlania i edytowania tekstu
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        # Przycisk "Otwórz plik"
        openButton = QPushButton("Otwórz plik")
        openButton.clicked.connect(self.openFile)
        layout.addWidget(openButton)

        # Przycisk "Zapisz plik"
        saveButton = QPushButton("Zapisz plik")
        saveButton.clicked.connect(self.saveFile)
        layout.addWidget(saveButton)

        # Przycisk "Wyczyść notatnik"
        clearButton = QPushButton("Wyczyść notatnik")
        clearButton.clicked.connect(self.clearText)
        layout.addWidget(clearButton)

        tab.setLayout(layout)
        return tab

    # Funkcja otwierania pliku
    def openFile(self):
        # Otwieranie pliku tekstowego
        fileName, _ = QFileDialog.getOpenFileName(self, "Otwórz plik", "", "Pliki tekstowe (*.txt)")
        self.fileNameG = fileName
        if fileName:
            with open(fileName, 'r') as file:
                content = file.read()
                self.textEdit.setText(content)

    # Funkcja zapisu pliku
    def saveFile(self):
        # Zapis zawartości do pliku tekstowego
        fileName, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "Pliki tekstowe (*.txt)")
        if fileName:
            with open(fileName, 'w') as file:
                content = self.textEdit.toPlainText()
                file.write(content)

    # Funkcja czyszczenia pola tekstowego
    def clearText(self):
        self.textEdit.clear()

    def saveFileSame(self):
        if self.fileNameG:
            with open(self.fileNameG, 'w') as file:
                content = self.textEdit.toPlainText()
                file.write(content)

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

    def clearAll3(self):
        self.textA.clear()
        self.textB.clear()
        self.numC.clear()
        self.resultField.clear()

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
