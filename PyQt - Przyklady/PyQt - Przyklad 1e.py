# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QGridLayout, QMessageBox, QPushButton

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
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Przycisk zostal nacisniety!')
    alert.exec()


# Stworzenie przycisku
button = QPushButton("To jest przycisk")

# Przypisanie do przycisku funkcji on_button_clicked
button.clicked.connect(on_button_clicked)

# Tworzenie prostego tekstu do wyświetlenia
label_1 = QLabel("Tekst z pierwszego okna")

# Tworzenie drugiego tekstu do wyświetlenia
label_2 = QLabel("Tekst z drugiego okna")

# Tworzenie layoutu (dostępne są również inne typy layoutów np. rozmieszczające elementy automatycznie w pionie lub poziomie: QHBoxLayout, QVBoxLayout)
layout = QGridLayout()

# Dodanie pierwszego elementu do layoutu - do lewego górnego rogu
layout.addWidget(label_1,0,0) 

# Dodanie drugiego elementu do layoutu - do prawego górnego rogu
layout.addWidget(label_2,0,1) 

# Dodanie przycisku do layoutu
layout.addWidget(button,1,0) 

# Podłączenie stworzonego layoutu do widżetu
window.setLayout(layout)

# Wyświetlenie widżetu
window.show()
app.exec()


