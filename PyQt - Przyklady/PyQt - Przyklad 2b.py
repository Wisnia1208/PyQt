from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap

app = QApplication([])
widget = QWidget()

widget.setWindowTitle("PyQt6 Lab")


# Stworzenie okna do wyboru pliku, zwracającego scieżkę do wybranego pliku 
fileName, selectedFilter = QFileDialog.getOpenFileName(widget, "Wybierz plik obrazu",  "Początkowa nazwa pliku", "All Files (*);;Python Files (*.py);; PNG (*.png)")

# Jeżeli nazwa została zwrócona (użytkownik wybrał plik), wyświetlenie obrazu za pomocą QPixmap
if fileName:
    label = QLabel(widget)
    pixmap = QPixmap(fileName)
    label.setPixmap(pixmap)
    widget.resize(pixmap.width(),pixmap.height())    

widget.show()
app.exec()
