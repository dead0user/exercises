# -*- coding: utf-8 -*-
# !/usr/bin/python

import random
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QMessageBox, QListWidget, QSpinBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Prosty generator rzutu kostką'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(600, 200, 340, 240)
        # self.setWindowIcon(QIcon('dice.png'))

        # lista rzutów
        self.listaRzutow = QListWidget(self)
        self.listaRzutow.move(10, 10)
        self.listaRzutow.resize(140, 220)

        # licznik do wpisywania liczby rzutów
        self.line = QSpinBox(self)
        self.line.move(245, 170)
        self.line.resize(40, 20)

        # wybór kostki za pomocą radiobuttonów
        self.k4 = QRadioButton('K4', self)
        self.k4.move(160, 10)
        self.k4.resize(96, 20)

        self.k6 = QRadioButton('K6', self)
        self.k6.move(160, 37)
        self.k6.resize(96, 20)
        self.k6.setChecked(True)

        self.k10 = QRadioButton('K10', self)
        self.k10.move(160, 63)
        self.k10.resize(96, 20)

        self.k12 = QRadioButton('K12', self)
        self.k12.move(160, 89)
        self.k12.resize(96, 20)

        self.k20 = QRadioButton('K20', self)
        self.k20.move(160, 115)
        self.k20.resize(96, 20)

        self.k100 = QRadioButton('K100', self)
        self.k100.move(160, 141)
        self.k100.resize(96, 20)

        # etykiety
        self.count = QLabel('Liczba rzutów:', self)
        self.count.move(160, 170)
        self.count.resize(80, 16)

        self.row1 = QLabel('Klawiszologia:', self)
        self.row1.move(230, 10)
        self.row1.resize(80, 16)

        self.row2 = QLabel('- wyjdź: Esc', self)
        self.row2.move(230, 35)
        self.row2.resize(100, 16)

        self.row3 = QLabel('- losuj: L', self)
        self.row3.move(230, 60)
        self.row3.resize(100, 16)

        self.row4 = QLabel('- czyść: C', self)
        self.row4.move(230, 85)
        self.row4.resize(100, 16)

        # przyciski
        self.rand = QPushButton('Losuj', self)
        self.rand.move(160, 200)
        self.rand.resize(84, 30)

        self.exit = QPushButton('Wyjdź', self)
        self.exit.move(250, 200)
        self.exit.resize(84, 30)

        self.line.setFocus()

        # zamknięcie aplikacji przyciskiem
        self.exit.clicked.connect(self.koniec)

        self.rand.clicked.connect(self.rzutKostka)

        self.show()

        # funkcja generująca rzuty na podstawie wprowadzonych danych

    def rzutKostka(self):
        ''' NOTE: właściwie przechwytywanie wyjątków nie jest już potrzebne, ponieważ pole QSpinBox jest liczbowe i pozwala zdefiniować dozwolony zakres '''
        try:
            # pobranie ilości rzutów z pola SpinBox
            ileRzutow = int(self.line.text())
# stany radiobuttonów / wybór kości
            if self.k4.isChecked():
                kosc = 4
            elif self.k6.isChecked():
                kosc = 6
            elif self.k10.isChecked():
                kosc = 10
            elif self.k12.isChecked():
                kosc = 12
            elif self.k20.isChecked():
                kosc = 20
            elif self.k100.isChecked():
                kosc = 100
            else:
                pass
# generowanie zestawu rzutów
            self.listaRzutow.clear()

            if ileRzutow > 0:
                # os.system("clear")
                for i in range(int(ileRzutow)):
                    wynik = str("Rzut " + str(i + 1) + ":	" + str(random.randrange(1, int(kosc) + 1, 1)))
                    self.listaRzutow.addItem(wynik)

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Nieprawidłowe dane. Wpisz liczbę całkowitą dodatnią.", QMessageBox.Ok)

    def koniec(self):
        self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(
            self, 'Komunikat',
            "Na pewno zamknąć?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# obsługa klawiszami
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_L:
            self.rzutKostka()
        if e.key() == Qt.Key_C:
            self.listaRzutow.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
