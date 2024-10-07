# Dołączenie modułów QApplication, QLabel z pakietu PyQt5.QtWidgets
from PyQt6.QtWidgets import QApplication, QLabel

# Inicjalizacja okna aplikacji
app = QApplication([])

# Tworzenie prostego pola tekstowego do wyświetlenia
label_1 = QLabel("Tekst z pierwszego okna")

# Tworzenie drugiego pola tekstowego do wyświetlenia
label_2 = QLabel("Tekst z drugiego okna")

# Wyświetlenie pól tekstowych

label_1.show()
label_2.show()
app.exec()




