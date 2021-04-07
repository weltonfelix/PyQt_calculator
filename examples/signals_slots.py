import sys
import getpass

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def greeting(who):
	if msg.text():
		msg.setText('')
	else:
		msg.setText(f'Hello {who}!')


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

button = QPushButton('Greet')
button.clicked.connect(lambda: greeting(getpass.getuser()))
layout.addWidget(button)

msg = QLabel('')
layout.addWidget(msg)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
