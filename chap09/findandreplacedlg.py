#!/usr/bin/env python3
# Copyright (c) 2008-10 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import chap09.ui_findandreplacedlg as ui_findandreplacedlg


class FindAndReplaceDlg(QDialog,
        ui_findandreplacedlg.Ui_FindAndReplaceDlg):

    def __init__(self, parent=None):
        super(FindAndReplaceDlg, self).__init__(parent)
        self.setupUi(self)
        self.moreFrame.hide()
        self.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.updateUi()


    # @pyqtSignature("QString")
    @pyqtSlot()
    def on_findLineEdit_textEdited(self, text):
        self.updateUi()


    # @pyqtSignature("")
    @pyqtSlot()
    def on_findButton_clicked(self):
        self.find.emit(self.findLineEdit.text(),
                       self.findLineEdit.text(),
                    self.caseCheckBox.isChecked(),
                    self.wholeCheckBox.isChecked(),
                    self.backwardsCheckBox.isChecked(),
                    self.regexCheckBox.isChecked(),
                    self.ignoreNotesCheckBox.isChecked())
        # self.emit(SIGNAL("find"), self.findLineEdit.text(),
        #         self.caseCheckBox.isChecked(),
        #         self.wholeCheckBox.isChecked(),
        #         self.backwardsCheckBox.isChecked(),
        #         self.regexCheckBox.isChecked(),
        #         self.ignoreNotesCheckBox.isChecked())
        
        
    # @pyqtSignature("")
    @pyqtSlot()
    def on_replaceButton_clicked(self):
        self.replace.emit(self.findLineEdit.text(),
                self.replaceLineEdit.text(),
                self.caseCheckBox.isChecked(),
                self.wholeCheckBox.isChecked(),
                self.backwardsCheckBox.isChecked(),
                self.regexCheckBox.isChecked(),
                self.ignoreNotesCheckBox.isChecked())
        # self.emit(SIGNAL("replace"), self.findLineEdit.text(),
        #         self.replaceLineEdit.text(),
        #         self.caseCheckBox.isChecked(),
        #         self.wholeCheckBox.isChecked(),
        #         self.backwardsCheckBox.isChecked(),
        #         self.regexCheckBox.isChecked(),
        #         self.ignoreNotesCheckBox.isChecked())
        

    def updateUi(self):
        enable = bool(self.findLineEdit.text())
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)



if __name__ == "__main__":
    import sys

    def find(what, *args):
        print("Find {} {}".format(what, [x for x in args]))

    def replace(old, new, *args):
        print("Replace {} with {} {}".format(
              old, new, [x for x in args]))

    app = QApplication(sys.argv)
    form = FindAndReplaceDlg()
    # form.find.connect(find)
    # form.connect(form, SIGNAL("find"), find)
    # form.replace.connect(replace)
    # form.connect(form, SIGNAL("replace"), replace)
    form.show()
    app.exec_()

