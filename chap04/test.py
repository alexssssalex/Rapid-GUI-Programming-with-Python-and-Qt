from PyQt5.QtWidgets import *
import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # date = self.getdata()
        self.rates = {'1 y':1.0,'2 y':2,'3 y':3}

        self.spinbox1 = QSpinBox()
        self.spinbox1.setRange(1, 1000)
        self.spinbox1.setValue(500)
        self.spinbox1.setSuffix(' $')

        self.spinbox2 = QSpinBox()
        self.spinbox2.setRange(1, 10)
        self.spinbox2.setValue(2.00)
        self.spinbox2.setSuffix(' %')

        self.box = QComboBox()
        self.box.addItems(self.rates)

        self.label = QLabel('#####')

        layout = QGridLayout()
        layout.addWidget(QLabel('Interes'), 0 ,0)
        layout.addWidget(self.spinbox1, 0, 1)
        layout.addWidget(QLabel('Proc'), 1 ,0)
        layout.addWidget(self.spinbox2, 1, 1)
        layout.addWidget(QLabel('year'), 2 ,0)
        layout.addWidget(self.box, 2, 1)
        layout.addWidget(QLabel('res'), 3 ,0)
        layout.addWidget(self.label, 3, 1)

        self.spinbox1.valueChanged.connect(self.result)
        self.spinbox2.valueChanged.connect(self.result)
        self.box.currentIndexChanged.connect(self.result)

        self.setLayout(layout)

    def result(self):
        d = self.spinbox1.value()*self.spinbox2.value()*self.rates[self.box.currentText()]
        # print(d)
        self.label.setText(str(d))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()