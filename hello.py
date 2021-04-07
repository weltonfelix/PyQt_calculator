import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Calculator")
window.setGeometry(0, 0, 300, 200)

text = QLabel("<h1>Hello, world!</h1>", parent=window)
text.move(60, 15)

window.show()

sys.exit(app.exec_())
