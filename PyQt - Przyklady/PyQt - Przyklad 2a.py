from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog

app = QApplication([])
widget = QWidget()

widget.setWindowTitle("PyQt6 Lab")

# Stworzenie okna do wyboru pliku, zwracającego scieżkę do wybranego pliku 
fileName, selectedFilter = QFileDialog.getOpenFileName(widget, "Wybierz plik obrazu",  "Początkowa nazwa pliku", "All Files (*);;Python Files (*.py);; PNG (*.png)")

# Jeżeli nazwa została zwrócona (użytkownik wybrał plik) - wyświetlenie nazwy
if fileName:
    print(fileName)
    
widget.show()
app.exec()


