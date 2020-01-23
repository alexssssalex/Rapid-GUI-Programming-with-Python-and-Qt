

import math
import random
import string
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numberformatdlg1
import numberformatdlg2
import numberformatdlg3


class Form1(QDialog):

    def __init__(self, parent=None):
        super(Form1, self).__init__(parent)
        bts = QDialogButtonBox(Qt.Vertical)
        self.lab = QLabel('Fruit')
        self.edit = QLineEdit()
        bts = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Close)
        layout = QVBoxLayout()
        layout.addWidget(self.lab)
        layout.addWidget(self.edit)
        layout.addWidget(bts)
        self.setLayout(layout)
        bts.rejected.connect(self.close)
        bts.accepted.connect(self.apply)

    def apply(self):
        print(self.edit.text())
        self.close()



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        bts = QDialogButtonBox(Qt.Vertical)
        add = bts.addButton("Add", QDialogButtonBox.HelpRole)
        bts.addButton("Edit", QDialogButtonBox.HelpRole)
        rem = bts.addButton("Remove", QDialogButtonBox.HelpRole)
        up = bts.addButton("Up", QDialogButtonBox.HelpRole)
        down = bts.addButton("Down", QDialogButtonBox.HelpRole)
        sort = bts.addButton("Sort", QDialogButtonBox.HelpRole)
        bts.addButton("Close", QDialogButtonBox.RejectRole)
        self.lst = QListWidget()
        self.lst.addItems(['orange','apple','banas'])
        # lst.addItem('bananas')
        layout = QHBoxLayout()
        layout.addWidget(self.lst)
        layout.addWidget(bts)
        self.setLayout(layout)

        sort.clicked.connect(self._sort)
        up.clicked.connect(self._up)
        down.clicked.connect(self._down)
        rem.clicked.connect(self._rem)
        bts.rejected.connect(self.close)
        add.clicked.connect(self._add)

    def _add(self):
        f = Form1()
        if f.exec_():
            print('aa')

    def _rem(self):
        currentRow = self.lst.currentRow()
        self.lst.takeItem(currentRow)

    def _sort(self):
        self.lst.sortItems()

    def _up(self):
        currentRow = self.lst.currentRow()
        if currentRow != 0:
            currentItem = self.lst.takeItem(currentRow)
            self.lst.insertItem(currentRow - 1, currentItem)
            self.lst.setCurrentRow(currentRow - 1)

    def _down(self):
        rows = self.lst.count()
        currentRow = self.lst.currentRow()
        if currentRow != rows-1:
            currentItem = self.lst.takeItem(currentRow)
            self.lst.insertItem(currentRow + 1, currentItem)
            self.lst.setCurrentRow(currentRow + 1)





app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()