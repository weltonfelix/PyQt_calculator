import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout

ERROR_MSG = 'ERROR'


class PyCalcUi(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('PyCalc')
		self.setFixedSize(235, 235)

		self.generalLayout = QVBoxLayout()

		self._centralWidget = QWidget(self)
		self.setCentralWidget(self._centralWidget)
		self._centralWidget.setLayout(self.generalLayout)

		self._createDisplay()
		self._createButtons()

	def _createDisplay(self):
		self.display = QLineEdit()
		self.display.setFixedHeight(35)
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)

		self.generalLayout.addWidget(self.display)

	def _createButtons(self):
		self.buttons = {}
		buttonsLayout = QGridLayout()

		buttonList = {
			'7': (0, 0),
			'8': (0, 1),
			'9': (0, 2),
			'/': (0, 3),
			'C': (0, 4),
			'4': (1, 0),
			'5': (1, 1),
			'6': (1, 2),
			'*': (1, 3),
			'(': (1, 4),
			'1': (2, 0),
			'2': (2, 1),
			'3': (2, 2),
			'-': (2, 3),
			')': (2, 4),
			'0': (3, 0),
			'00': (3, 1),
			'.': (3, 2),
			'+': (3, 3),
			'=': (3, 4),
		}

		for buttonText, pos in buttonList.items():
			self.buttons[buttonText] = QPushButton(buttonText)
			self.buttons[buttonText].setFixedSize(40, 40)

			buttonsLayout.addWidget(self.buttons[buttonText], pos[0], pos[1])

		self.generalLayout.addLayout(buttonsLayout)

	def setDisplayText(self, text):
		self.display.setText(text)
		self.display.setFocus()

	def displayText(self):
		return self.display.text()

	def clearDisplay(self):
		self.display.clear()


class PyCalcController:
	def __init__(self, model, view):
		self._model = model
		self._view = view
		self._connectSignals()

	def _calculateResult(self):
		result = self._model.evaluateExpression(self._view.displayText())
		self._view.setDisplayText(result)

	def _buildExpression(self, subExpression):
		if self._view.displayText() == ERROR_MSG:
			self._view.clearDisplay()

		expression = self._view.displayText() + subExpression
		self._view.setDisplayText(expression)

	def _connectSignals(self):
		for buttonText, button in self._view.buttons.items():
			if buttonText not in {'=', 'C'}:
				button.clicked.connect(partial(self._buildExpression, buttonText))

		self._view.buttons['='].clicked.connect(self._calculateResult)
		self._view.display.returnPressed.connect(self._calculateResult)
		self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


class PyCalcModel:
	@staticmethod
	def evaluateExpression(expression):
		try:
			result = str(eval(expression, {}, {}))
		except Exception:
			result = ERROR_MSG

		return result


def main():
	pycalc = QApplication(sys.argv)

	view = PyCalcUi()
	view.show()

	PyCalcController(model=PyCalcModel, view=view)

	sys.exit(pycalc.exec())


if __name__ == '__main__':
	main()
