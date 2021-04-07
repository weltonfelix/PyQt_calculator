import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QGridLayout")

layout = QGridLayout()
layout.addWidget(QPushButton('A1'), 0, 0)
layout.addWidget(QPushButton('B1'), 0, 1)
layout.addWidget(QPushButton('C1'), 0, 2)
layout.addWidget(QPushButton('A2'), 1, 0)
layout.addWidget(QPushButton('B2'), 1, 1)
layout.addWidget(QPushButton('C2'), 1, 2)
layout.addWidget(QPushButton('A3'), 2, 0)
layout.addWidget(QPushButton('B3 + C3'), 2, 1, 1, 2)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
