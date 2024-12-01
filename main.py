import sqlite3
import sys
from PyQt6 import uic

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        queue = "SELECT * FROM Coffes"
        queue = cur.execute(queue).fetchall()
        self.tableWidget.setRowCount(len(queue))
        if not queue:
            return
        self.tableWidget.setColumnCount(len(queue[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(queue):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())