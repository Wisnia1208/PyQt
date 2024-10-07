# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel

# Inicjalizacja okna aplikacji
app = QApplication([])

# Tworzenie prostego pola tekstowego do wyświetlenia
label = QLabel("Tekst w pierwszej aplikacji okienkowej")

# Wyświetlenie pola tekstowego
label.show()
app.exec()



