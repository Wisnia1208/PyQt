# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

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

# Tworzenie prostego tekstu do wyświetlenia
label_1 = QLabel("Tekst z pierwszego okna", parent=window)

# Tworzenie drugiego tekstu do wyświetlenia
label_2 = QLabel("Tekst z drugiego okna", parent=window)

# Wyświetlenie widżetu
window.show()
app.exec()



