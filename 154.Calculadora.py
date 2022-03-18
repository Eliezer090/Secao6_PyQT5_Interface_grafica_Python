import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QGridLayout, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget(self)
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit(self.cw)
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background-color: white; color: #000; font-size: 20px; font-family: Arial, Helvetica, sans-serif;}')

        self.add_btn(QPushButton('7', self.cw), 1, 0)
        self.add_btn(QPushButton('8', self.cw), 1, 1)
        self.add_btn(QPushButton('9', self.cw), 1, 2)
        self.add_btn(QPushButton('+', self.cw), 1, 3)
        self.add_btn(QPushButton('C', self.cw), 1, 4, 1,
                     1, lambda: self.display.setText(''))

        self.add_btn(QPushButton('4', self.cw), 2, 0)
        self.add_btn(QPushButton('5', self.cw), 2, 1)
        self.add_btn(QPushButton('6', self.cw), 2, 2)
        self.add_btn(QPushButton('-', self.cw), 2, 3)
        self.add_btn(QPushButton('<-', self.cw), 2, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]))

        self.add_btn(QPushButton('1', self.cw), 3, 0)
        self.add_btn(QPushButton('2', self.cw), 3, 1)
        self.add_btn(QPushButton('3', self.cw), 3, 2)
        self.add_btn(QPushButton('/', self.cw), 3, 3)
        self.add_btn(QPushButton('=', self.cw), 3, 4, 1, 1, self.eval_igual)

        self.add_btn(QPushButton('.', self.cw), 4, 0)
        self.add_btn(QPushButton('0', self.cw), 4, 1)
        self.add_btn(QPushButton('', self.cw), 4, 2)
        self.add_btn(QPushButton('*', self.cw), 4, 3)
        self.add_btn(QPushButton('', self.cw), 4, 4)
        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan=1, colspan=1, funcao=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if funcao:
            btn.clicked.connect(funcao)
        else:
            btn.clicked.connect(lambda: self.display.setText(
                self.display.text() + btn.text()))
        btn.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except:
            self.display.setText('Erro na expressão')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    ex = Calculadora()
    ex.show()
    sys.exit(qt.exec_())
