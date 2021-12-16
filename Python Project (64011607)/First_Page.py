from PyQt5 import QtCore, QtGui, QtWidgets
from Rule_Page import Ui_Rule
from Play_Page import Ui_Form



class Ui_page(object):
    def openWindow1(self):
        self.window1 = QtWidgets.QWidget()
        self.ui = Ui_Rule()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def openWindow2(self):
        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi2(self.window2)
        self.window2.show()
    def setupUi(self, page):
        page.setObjectName("page")
        page.resize(710, 431)
        page.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0.523, x2:1, y2:0.534, stop:0 rgba(255, 73, 76, 255), stop:1 rgba(156, 255, 255, 255))")
        self.labelSic = QtWidgets.QLabel(page)
        self.labelSic.setGeometry(QtCore.QRect(0, 70, 711, 161))
        self.labelSic.setObjectName("labelSic")
        self.p_play = QtWidgets.QPushButton(page)
        self.p_play.setGeometry(QtCore.QRect(290, 260, 141, 71))
        self.p_play.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.p_play.setObjectName("p_play")
        self.p_play.clicked.connect(self.openWindow2)
        self.p_rule = QtWidgets.QPushButton(page)
        self.p_rule.setGeometry(QtCore.QRect(250, 350, 221, 51))
        self.p_rule.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.p_rule.setObjectName("p_rule")
        self.p_rule.clicked.connect(self.openWindow1)

        self.retranslateUi(page)
        QtCore.QMetaObject.connectSlotsByName(page)

    def retranslateUi(self, page):
        _translate = QtCore.QCoreApplication.translate
        page.setWindowTitle(_translate("page", "Form"))
        self.labelSic.setText(_translate("page", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#0000ff;\">SicBo</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#0000ff;\">Casino by KMITL</span></p></body></html>"))
        self.p_play.setText(_translate("page", "PLAY !"))
        self.p_rule.setText(_translate("page", "Rules ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page = QtWidgets.QWidget()
    ui = Ui_page()
    ui.setupUi(page)
    page.show()
    sys.exit(app.exec_())
