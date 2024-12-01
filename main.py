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
        self.save_b.clicked.connect(self.adding)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.edit_b.clicked.connect(self.eding)

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
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()
        self.update_result()

    def eding(self):
        self.add_form = AddWidget(self, 1)
        self.add_form.show()
        self.update_result()


class AddWidget(QMainWindow):
    def __init__(self, parent=None, a=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.cur = parent.con.cursor()
        self.parent = parent
        print(self.parent.modified.keys())
        if not a:
            self.pushButton.clicked.connect(self.get_adding_verdict)
        else:
            self.modified = parent.modified
            self.pushButton.clicked.connect(self.f)

    def f(self):
        try:
            name = '"' + self.name.text() + '"'
            price = self.prise.text()
            valume = self.valume.text()
            description = '"' + self.description.text() + '"'
            roasting = '"' + self.roasting.text() + '"'
            gog = '"' + self.gog.text() + '"'
            s = [name, roasting, gog, description, price, valume]
            s1 = ['name', 'Roasting', 'ground_or_grains', 'description', 'prise', 'volume']

            que = "UPDATE Coffes SET\n"

            que += ', '.join([f"{s1[i]}={s[i]}" for i in range(len(s))])
            que = que + "WHERE" + " AND ".join([f"{key}='{self.modified.get(key)}'" for key in self.modified.keys()])
            self.parent.cur.execute(que)
            self.parent.con.commit()
            self.close()
        except Exception:
            return False


    def get_adding_verdict(self):
        try:
            name = '"' + self.name.text() + '"'
            price = self.prise.text()
            valume = self.valume.text()
            description = '"' + self.description.text() + '"'
            roasting = '"' + self.roasting.text() + '"'
            gog = '"' + self.gog.text() + '"'
            s = [name, roasting, gog, description, price, valume]
            q = f'''INSERT INTO Coffes(name, Roasting, ground_or_grains, description, prise, volume)
            VALUES({', '.join(s)})'''
            self.parent.cur.execute(q)
            self.parent.con.commit()
            self.close()
        except Exception:
            return False
        return True


    def get_adding_verdict(self):
        try:
            name = '"' + self.name.text() + '"'
            price = self.prise.text()
            valume = self.valume.text()
            description = '"' + self.description.text() + '"'
            roasting = '"' + self.roasting.text() + '"'
            gog = '"' + self.gog.text() + '"'
            s = [name, roasting, gog, description, price, valume]
            q = f'''INSERT INTO Coffes(name, Roasting, ground_or_grains, description, prise, volume)
            VALUES({', '.join(s)})'''
            self.parent.cur.execute(q)
            self.parent.con.commit()
            self.close()
        except Exception:
            return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())