import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
	    super().__init__()
	    self.title = 'Hello World'
	    self.left = 200
	    self.top = 100
	    self.width = 200
	    self.height = 200
	    self.initUI()

    def initUI(self):
	    self.setWindowTitle(self.title)
	    self.setGeometry(self.left, self.top, self.width, self.height)

	    self.label = QLabel("Hello World", self)
	    self.label.move(60,80)
	    self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
