import sys
from PyQt5.QtWidgets import QApplication, QMainwindow
from PyQt5.QtGui import QIcon

class Mainindow(QMainwindow) :
    def __init__(self):
        super.__init__()
        self.setWindowTitle("POGG!!")
        self.setGeometry(700,300,500,500)

    def main() : 
        app = QApplication(sys.argv)
        window = Mainindow()
        window.show()
        sys.exit(app.exec_())

    if __name__ == "__main__" : 
        main()