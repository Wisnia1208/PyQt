# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox

# Inicjalizacja okna aplikacji
app = QApplication([])

# Tworzenie widżetu przechowującego elementy interfejsu (np. pola tekstowe)
window = QWidget()

# Ustawienie tytułu okna
window.setWindowTitle('PyQt6 Lab')

# Ustawienie wielkości okna
window.setGeometry(100, 100, 280, 80)

# Ustawienie pozycji początkowej okna
window.move(60, 15)

# Stworzenie funkcji wyświetlającej MessageBox'a
def on_text_1_changed():
    alert = QMessageBox()
    alert.setText('Tekst 1 został zmieniony')
    alert.exec()

# Tworzenie pola do wprowadzania tekstu 
text_1 = QPlainTextEdit()
text_1.insertPlainText("Tutaj wpisz swój tekst.\n")
text_1.resize(400,200)

# Połączenie funkcji on_text_1_changed ze zdarzeniem zmiany tekstu w polu tekstowym
text_1.textChanged.connect(on_text_1_changed)

# Tworzenie layoutu (dostępne są również inne typy layoutów np. rozmieszczające elementy automatycznie w pionie lub poziomie: QHBoxLayout, QVBoxLayout)
layout = QGridLayout()

# Dodanie pola tekstowego 
layout.addWidget(text_1,0,0) 

# Podłączenie stworzonego layoutu do widżetu
window.setLayout(layout)

# Wyświetlenie widżetu
window.show()
app.exec()
