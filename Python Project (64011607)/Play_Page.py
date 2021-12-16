from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Form(object):
    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 459)
        Form.setStyleSheet("background-color :qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.505818, stop:0 rgba(170, 255, 255, 255), stop:1 rgba(169, 255, 255, 255))")
        self.p_0 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("0"))
        self.p_0.setGeometry(QtCore.QRect(40, 210, 31, 41))
        self.p_0.setStyleSheet("font: 25pt \"Times\";")
        self.p_0.setObjectName("p_0")
        self.p_1 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("1"))
        self.p_1.setGeometry(QtCore.QRect(40, 90, 31, 41))
        self.p_1.setStyleSheet("font: 25pt \"Times\";")
        self.p_1.setObjectName("p_1")
        self.p_2 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("2"))
        self.p_2.setGeometry(QtCore.QRect(70, 90, 31, 41))
        self.p_2.setStyleSheet("font: 25pt \"Times\";")
        self.p_2.setObjectName("p_2")
        self.p_3 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("3"))
        self.p_3.setGeometry(QtCore.QRect(100, 90, 31, 41))
        self.p_3.setStyleSheet("font: 25pt \"Times\";")
        self.p_3.setObjectName("p_3")
        self.p_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("4"))
        self.p_4.setGeometry(QtCore.QRect(40, 130, 31, 41))
        self.p_4.setStyleSheet("font: 25pt \"Times\";")
        self.p_4.setObjectName("p_4")
        self.p_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("5"))
        self.p_5.setGeometry(QtCore.QRect(70, 130, 31, 41))
        self.p_5.setStyleSheet("font: 25pt \"Times\";")
        self.p_5.setObjectName("p_5")
        self.p_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("6"))
        self.p_6.setGeometry(QtCore.QRect(100, 130, 31, 41))
        self.p_6.setStyleSheet("font: 25pt \"Times\";")
        self.p_6.setObjectName("p_6")
        self.p_7 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("7"))
        self.p_7.setGeometry(QtCore.QRect(40, 170, 31, 41))
        self.p_7.setStyleSheet("font: 25pt \"Times\";")
        self.p_7.setObjectName("p_7")
        self.p_8 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("8"))
        self.p_8.setGeometry(QtCore.QRect(70, 170, 31, 41))
        self.p_8.setStyleSheet("font: 25pt \"Times\";")
        self.p_8.setObjectName("p_8")
        self.p_9 = QtWidgets.QPushButton(Form, clicked= lambda: self.press("9"))
        self.p_9.setGeometry(QtCore.QRect(100, 170, 31, 41))
        self.p_9.setStyleSheet("font: 25pt \"Times\";")
        self.p_9.setObjectName("p_9")
        self.p_c = QtWidgets.QPushButton(Form, clicked= lambda: self.something("Clear"))
        self.p_c.setGeometry(QtCore.QRect(70, 210, 61, 21))
        self.p_c.setStyleSheet("font: 10pt \"Times\";")
        self.p_c.setObjectName("p_c")
        self.p_ce = QtWidgets.QPushButton(Form, clicked= lambda: self.something("Delete"))
        self.p_ce.setGeometry(QtCore.QRect(70, 230, 61, 21))
        self.p_ce.setStyleSheet("font: 10pt \"Times\";")
        self.p_ce.setObjectName("p_ce")

        self.l_l = QtWidgets.QLabel(Form)
        self.l_l.setGeometry(QtCore.QRect(40, 40, 131, 31))
        self.l_l.setStyleSheet("font: 75 20pt \"Times\";")
        self.l_l.setObjectName("l_l")
        self.l_all = QtWidgets.QLabel(Form)
        self.l_all.setGeometry(QtCore.QRect(40, 260, 131, 41))
        self.l_all.setStyleSheet("font: 75 15pt \"Times\";")        
        self.l_all.setObjectName("l_all")

        self.p_high = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("High"))
        self.p_high.setGeometry(QtCore.QRect(420, 40, 241, 51))
        self.p_high.setStyleSheet("font: 75 20pt \"Times\";")
        self.p_high.setObjectName("p_high")
        self.p_low = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Low"))
        self.p_low.setGeometry(QtCore.QRect(180, 40, 241, 51))
        self.p_low.setStyleSheet("font: 75 20pt \"Times\";")
        self.p_low.setObjectName("p_low")

        self.n_19 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet3"))
        self.n_19.setGeometry(QtCore.QRect(180, 90, 31, 91))
        self.n_19.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_19.setObjectName("n_19")
        self.n_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet4"))
        self.n_4.setGeometry(QtCore.QRect(210, 90, 31, 91))
        self.n_4.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_4.setObjectName("n_4")
        self.n_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet5"))
        self.n_5.setGeometry(QtCore.QRect(240, 90, 31, 91))
        self.n_5.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_5.setObjectName("n_5")
        self.n_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet6"))
        self.n_6.setGeometry(QtCore.QRect(270, 90, 31, 91))
        self.n_6.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_6.setObjectName("n_6")
        self.n_7 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet7"))
        self.n_7.setGeometry(QtCore.QRect(300, 90, 31, 91))
        self.n_7.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_7.setObjectName("n_7")
        self.n_8 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet8"))
        self.n_8.setGeometry(QtCore.QRect(330, 90, 31, 91))
        self.n_8.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_8.setObjectName("n_8")
        self.n_9 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet9"))
        self.n_9.setGeometry(QtCore.QRect(360, 90, 31, 91))
        self.n_9.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_9.setObjectName("n_9")
        self.n_10 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet10"))
        self.n_10.setGeometry(QtCore.QRect(390, 90, 31, 91))
        self.n_10.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_10.setObjectName("n_10")
        self.n_11 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet11"))
        self.n_11.setGeometry(QtCore.QRect(420, 90, 31, 91))
        self.n_11.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_11.setObjectName("n_11")
        self.n_12 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet12"))
        self.n_12.setGeometry(QtCore.QRect(450, 90, 31, 91))
        self.n_12.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_12.setObjectName("n_12")
        self.n_13 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet13"))
        self.n_13.setGeometry(QtCore.QRect(480, 90, 31, 91))
        self.n_13.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_13.setObjectName("n_13")
        self.n_14 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet14"))
        self.n_14.setGeometry(QtCore.QRect(510, 90, 31, 91))
        self.n_14.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_14.setObjectName("n_14")
        self.n_15 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet15"))
        self.n_15.setGeometry(QtCore.QRect(540, 90, 31, 91))
        self.n_15.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_15.setObjectName("n_15")
        self.n_16 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet16"))
        self.n_16.setGeometry(QtCore.QRect(570, 90, 31, 91))
        self.n_16.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_16.setObjectName("n_16")
        self.n_17 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet17"))
        self.n_17.setGeometry(QtCore.QRect(600, 90, 31, 91))
        self.n_17.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_17.setObjectName("n_17")
        self.n_18 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Bet18"))
        self.n_18.setGeometry(QtCore.QRect(630, 90, 31, 91))
        self.n_18.setStyleSheet("font: 75 18pt \"Times\";")
        self.n_18.setObjectName("n_18")
        
        self.d_0 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double0"))
        self.d_0.setGeometry(QtCore.QRect(540, 220, 121, 61))
        self.d_0.setStyleSheet("font: 75 20pt \"Times\";")
        self.d_0.setObjectName("d_0")
        self.d_1 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double1"))
        self.d_1.setGeometry(QtCore.QRect(180, 220, 61, 61))
        self.d_1.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_1.setObjectName("d_1")
        self.d_2 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double2"))
        self.d_2.setGeometry(QtCore.QRect(240, 220, 61, 61))
        self.d_2.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_2.setObjectName("d_2")
        self.d_3 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double3"))
        self.d_3.setGeometry(QtCore.QRect(300, 220, 61, 61))
        self.d_3.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_3.setObjectName("d_3")
        self.d_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double4"))
        self.d_4.setGeometry(QtCore.QRect(360, 220, 61, 61))
        self.d_4.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_4.setObjectName("d_4")
        self.d_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double5"))
        self.d_5.setGeometry(QtCore.QRect(420, 220, 61, 61))
        self.d_5.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_5.setObjectName("d_5")
        self.d_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Double6"))
        self.d_6.setGeometry(QtCore.QRect(480, 220, 61, 61))
        self.d_6.setStyleSheet("font: 75 10pt \"Times\";")
        self.d_6.setObjectName("d_6")

        self.t_0 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple0"))
        self.t_0.setGeometry(QtCore.QRect(540, 280, 121, 61))
        self.t_0.setStyleSheet("font: 75 20pt \"Times\";")
        self.t_0.setObjectName("t_0")
        self.t_1 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple1"))
        self.t_1.setGeometry(QtCore.QRect(180, 280, 61, 61))
        self.t_1.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_1.setObjectName("t_1")
        self.t_2 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple2"))
        self.t_2.setGeometry(QtCore.QRect(240, 280, 71, 61))
        self.t_2.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_2.setObjectName("t_2")
        self.t_3 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple3"))
        self.t_3.setGeometry(QtCore.QRect(300, 280, 61, 61))
        self.t_3.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_3.setObjectName("t_3")    
        self.t_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple4"))
        self.t_4.setGeometry(QtCore.QRect(360, 280, 61, 61))
        self.t_4.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_4.setObjectName("t_4")
        self.t_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple5"))
        self.t_5.setGeometry(QtCore.QRect(420, 280, 61, 61))
        self.t_5.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_5.setObjectName("t_5")
        self.t_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Triple6"))
        self.t_6.setGeometry(QtCore.QRect(480, 280, 61, 61))
        self.t_6.setStyleSheet("font: 75 10pt \"Times\";")
        self.t_6.setObjectName("t_6")

        self.dice_1 = QtWidgets.QLabel(Form)
        self.dice_1.setGeometry(QtCore.QRect(700, 70, 61, 81))
        self.dice_1.setStyleSheet("font: 75 48pt \"Times\";")
        self.dice_1.setObjectName("dice_1")
        self.dice_2 = QtWidgets.QLabel(Form)
        self.dice_2.setGeometry(QtCore.QRect(700, 160, 61, 91))
        self.dice_2.setStyleSheet("font: 75 48pt \"Times\";")
        self.dice_2.setObjectName("dice_2")
        self.dice_3 = QtWidgets.QLabel(Form)
        self.dice_3.setGeometry(QtCore.QRect(700, 260, 61, 81))
        self.dice_3.setStyleSheet("font: 75 48pt \"Times\";")
        self.dice_3.setObjectName("dice_3")
        
        self.die_1 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("ONE"))
        self.die_1.setGeometry(QtCore.QRect(180, 180, 81, 41))
        self.die_1.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_1.setObjectName("die_1")
        self.die_2 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("TWO"))
        self.die_2.setGeometry(QtCore.QRect(260, 180, 81, 41))
        self.die_2.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_2.setObjectName("die_2")
        self.die_3 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("THREE"))
        self.die_3.setGeometry(QtCore.QRect(340, 180, 81, 41))
        self.die_3.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_3.setObjectName("die_3")
        self.die_4 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("FOUR"))
        self.die_4.setGeometry(QtCore.QRect(420, 180, 81, 41))
        self.die_4.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_4.setObjectName("die_4")
        self.die_5 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("FIVE"))
        self.die_5.setGeometry(QtCore.QRect(500, 180, 81, 41))
        self.die_5.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_5.setObjectName("die_5")   
        self.die_6 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("SIX"))
        self.die_6.setGeometry(QtCore.QRect(580, 180, 81, 41))
        self.die_6.setStyleSheet("font: 75 15pt \"Times\";")
        self.die_6.setObjectName("die_6")
        

        self.st123 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("r123"))
        self.st123.setGeometry(QtCore.QRect(180, 340, 121, 41))
        self.st123.setStyleSheet("font: 75 15pt \"Times\";")
        self.st123.setObjectName("st123")
        self.st234 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("r234"))
        self.st234.setGeometry(QtCore.QRect(300, 340, 121, 41))
        self.st234.setStyleSheet("font: 75 15pt \"Times\";")
        self.st234.setObjectName("st234")
        self.st345 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("r345"))
        self.st345.setGeometry(QtCore.QRect(420, 340, 121, 41))
        self.st345.setStyleSheet("font: 75 15pt \"Times\";")
        self.st345.setObjectName("st345")
        self.st456 = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("r456"))
        self.st456.setGeometry(QtCore.QRect(540, 340, 121, 41))
        self.st456.setStyleSheet("font: 75 15pt \"Times\";")
        self.st456.setObjectName("st456")

        self.oddd = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Odd"))
        self.oddd.setGeometry(QtCore.QRect(180, 380, 241, 41))
        self.oddd.setStyleSheet("font: 75 18pt \"Times\";")
        self.oddd.setObjectName("oddd")
        self.evenn = QtWidgets.QPushButton(Form, clicked= lambda: self.rolld("Even"))
        self.evenn.setGeometry(QtCore.QRect(420, 380, 241, 41))
        self.evenn.setStyleSheet("font: 75 17pt \"Times\";")
        self.evenn.setObjectName("evenn")

        self.rlist=[]
        self.rsum=0
        self.balance=1000
        self.result=""
        self.x=1
        self.bet=""

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.p_0.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_0.setText(_translate("Form", "0"))
        self.p_1.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_1.setText(_translate("Form", "1"))
        self.p_2.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_2.setText(_translate("Form", "2"))
        self.p_3.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_3.setText(_translate("Form", "3"))
        self.p_4.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_4.setText(_translate("Form", "4"))
        self.p_5.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_5.setText(_translate("Form", "5"))
        self.p_6.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_6.setText(_translate("Form", "6"))
        self.p_7.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_7.setText(_translate("Form", "7"))
        self.p_8.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_8.setText(_translate("Form", "8"))
        self.p_9.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.p_9.setText(_translate("Form", "9"))
        self.p_c.setText(_translate("Form", "Clear"))
        self.p_ce.setText(_translate("Form", "Delete"))
        self.l_l.setText(_translate("Form", "<html><head/><body><p>0</p></body></html>"))
        self.l_l.setText('0')
        self.l_all.setText(_translate("Form", "<html><head/><body><p>1000</p></body></html>"))
        self.l_all.setText(str(self.balance))

        self.p_high.setText(_translate("Form", "High"))
        self.p_low.setText(_translate("Form", "Low"))

        self.n_19.setText(_translate("Form", "3"))
        self.n_4.setText(_translate("Form", "4"))
        self.n_5.setText(_translate("Form", "5"))
        self.n_6.setText(_translate("Form", "6"))
        self.n_7.setText(_translate("Form", "7"))
        self.n_8.setText(_translate("Form", "8"))
        self.n_9.setText(_translate("Form", "9"))
        self.n_10.setText(_translate("Form", "10"))
        self.n_11.setText(_translate("Form", "11"))
        self.n_12.setText(_translate("Form", "12"))
        self.n_13.setText(_translate("Form", "13"))
        self.n_14.setText(_translate("Form", "14"))
        self.n_15.setText(_translate("Form", "15"))
        self.n_16.setText(_translate("Form", "16"))
        self.n_17.setText(_translate("Form", "17"))
        self.n_18.setText(_translate("Form", "18"))

        self.d_0.setText(_translate("Form", "Double"))
        self.d_1.setText(_translate("Form", "Double 1"))
        self.d_2.setText(_translate("Form", "Double 2"))
        self.d_3.setText(_translate("Form", "Double 3"))
        self.d_4.setText(_translate("Form", "Double 4"))
        self.d_5.setText(_translate("Form", "Double 5"))
        self.d_6.setText(_translate("Form", "Double 6"))
        self.t_0.setText(_translate("Form", "Triple"))
        self.t_1.setText(_translate("Form", "Triple 1"))
        self.t_2.setText(_translate("Form", "Triple 2"))
        self.t_3.setText(_translate("Form", "Triple 3"))
        self.t_4.setText(_translate("Form", "Triple 4"))
        self.t_5.setText(_translate("Form", "Triple 5"))
        self.t_6.setText(_translate("Form", "Triple 6"))
        self.dice_1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.dice_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.dice_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        
        self.die_1.setText(_translate("Form", "ONE"))
        self.die_2.setText(_translate("Form", "TWO"))
        self.die_3.setText(_translate("Form", "THREE"))
        self.die_4.setText(_translate("Form", "FOUR"))
        self.die_5.setText(_translate("Form", "FIVE"))        
        self.die_6.setText(_translate("Form", "SIX"))
        self.st123.setText(_translate("Form", "1 2 3"))
        self.st234.setText(_translate("Form", "2 3 4"))
        self.st345.setText(_translate("Form", "3 4 5"))
        self.st456.setText(_translate("Form", "4 5 6"))

        self.oddd.setText(_translate("Form", "Odd"))
        self.evenn.setText(_translate("Form", "Even"))



    def press(self, pressed):
        if self.balance != 0:

            if self.l_l.text() == '' or self.l_l.text() == '0':
                self.bet=pressed
                self.l_l.setText(self.bet) 
            else:
                self.bet += pressed
                self.l_l.setText(self.bet)
        else:
            self.l_all.setText("END")

    def something(self, pressed):
        screen = self.l_l.text()
        if pressed == "Delete":
            AAA = self.l_l.text()
            if len(screen) > 1:
                self.l_l.setText(AAA[:-1])
            else:
                self.l_l.setText('0')
        elif pressed == "Clear":
            self.l_l.setText("0")

    def rolld(self, pressed):
        if self.balance != 0:
            self.rlist.clear()
            a = random.randint(1,6)
            self.rlist.append(a)
            self.dice_1.setText(str(a))
            a = random.randint(1,6)
            self.rlist.append(a)
            self.dice_2.setText(str(a))
            a = random.randint(1,6)
            self.rlist.append(a)
            self.dice_3.setText(str(a))
            self.rsum=sum(self.rlist)
            if int(self.bet) <= self.balance:


                if (pressed == "High") and (self.rsum >= 11):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "Low") and (self.rsum <=10):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "3") and (self.rsum == 3):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "4") and (self.rsum == 4):
                    self.result = "win"
                    self.x = 60
                elif (pressed == "5") and (self.rsum == 5):
                    self.result = "win"
                    self.x = 20
                elif (pressed == "6") and (self.rsum == 6):
                    self.result = "win"
                    self.x = 18
                elif (pressed == "7") and (self.rsum == 7):
                    self.result = "win"
                    self.x = 12
                elif (pressed == "8") and (self.rsum == 8):
                    self.result = "win"
                    self.x = 8
                elif (pressed == "9") and (self.rsum == 9):
                    self.result = "win"
                    self.x = 6
                elif (pressed == "10") and (self.rsum == 10):
                    self.result = "win"
                    self.x = 6
                elif (pressed == "11") and (self.rsum == 11):
                    self.result = "win"
                    self.x = 6
                elif (pressed == "12") and (self.rsum == 12):
                    self.result = "win"
                    self.x = 6
                elif (pressed == "13") and (self.rsum == 13):
                    self.result = "win"
                    self.x = 8
                elif (pressed == "14") and (self.rsum == 14):
                    self.result = "win"
                    self.x = 12
                elif (pressed == "15") and (self.rsum == 15):
                    self.result = "win"
                    self.x = 18
                elif (pressed == "16") and (self.rsum == 16):
                    self.result = "win"
                    self.x = 20
                elif (pressed == "17") and (self.rsum == 17):
                    self.result = "win"
                    self.x = 60
                elif (pressed == "18") and (self.rsum == 18):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple0") and (self.rlist[0] == self.rlist[1] == self.rlist[2]):
                    self.result = "win"
                    self.x = 30
                elif (pressed == "Triple1") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 1):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple2") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 2):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple3") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 3):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple4") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 4):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple5") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 5):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Triple6") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 6):
                    self.result = "win"
                    self.x = 180
                elif (pressed == "Double0") and ((self.rlist[0] == self.rlist[1]) or (self.rlist[1] == self.rlist[2]) or (self.rlist[0] == self.rlist[2])):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "Double1") and ((self.rlist[0] == self.rlist[1] == 1) or (self.rlist[1] == self.rlist[2] == 1) or (self.rlist[0] == self.rlist[2] == 1)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "Double2") and ((self.rlist[0] == self.rlist[1] == 2) or (self.rlist[1] == self.rlist[2] == 2) or (self.rlist[0] == self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "Double3") and ((self.rlist[0] == self.rlist[1] == 3) or (self.rlist[1] == self.rlist[2] == 3) or (self.rlist[0] == self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "Double4") and ((self.rlist[0] == self.rlist[1] == 4) or (self.rlist[1] == self.rlist[2] == 4) or (self.rlist[0] == self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "Double5") and ((self.rlist[0] == self.rlist[1] == 5) or (self.rlist[1] == self.rlist[2] == 5) or (self.rlist[0] == self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "Double6") and ((self.rlist[0] == self.rlist[1] == 6) or (self.rlist[1] == self.rlist[2] == 6) or (self.rlist[0] == self.rlist[2] == 6)):
                    self.result = "win"
                    self.x = 11
                elif (pressed == "ONE") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 1):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "ONE") and ((self.rlist[0] == self.rlist[1] == 1) or (self.rlist[1] == self.rlist[2] == 1) or (self.rlist[0] == self.rlist[2] == 1)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "ONE") and ((self.rlist[0] == 1) or (self.rlist[1] == 1) or (self.rlist[2] == 1)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "TWO") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 2):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "TWO") and ((self.rlist[0] == self.rlist[1] == 2) or (self.rlist[1] == self.rlist[2] == 2) or (self.rlist[0] == self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "TWO") and ((self.rlist[0] == 2) or (self.rlist[1] == 2) or (self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "THREE") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 3):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "THREE") and ((self.rlist[0] == self.rlist[1] == 3) or (self.rlist[1] == self.rlist[2] == 3) or (self.rlist[0] == self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "THREE") and ((self.rlist[0] == 3) or (self.rlist[1] == 3) or (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "FOUR") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 4):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "FOUR") and ((self.rlist[0] == self.rlist[1] == 4) or (self.rlist[1] == self.rlist[2] == 4) or (self.rlist[0] == self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "FOUR") and ((self.rlist[0] == 4) or (self.rlist[1] == 4) or (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "FIVE") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 5):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "FIVE") and ((self.rlist[0] == self.rlist[1] == 5) or (self.rlist[1] == self.rlist[2] == 5) or (self.rlist[0] == self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "FIVE") and ((self.rlist[0] == 5) or (self.rlist[1] == 5) or (self.rlist[2] == 51)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "SIX") and (self.rlist[0] == self.rlist[1] == self.rlist[2] == 6):
                    self.result = "win"
                    self.x = 3
                elif (pressed == "SIX") and ((self.rlist[0] == self.rlist[1] == 6) or (self.rlist[1] == self.rlist[2] == 6) or (self.rlist[0] == self.rlist[2] == 6)):
                    self.result = "win"
                    self.x = 2
                elif (pressed == "SIX") and ((self.rlist[0] == 6) or (self.rlist[1] == 6) or (self.rlist[2] == 6)):
                    self.result = "win"
                    self.x = 1
                elif (pressed == "r123") and ((self.rlist[0] == 1) and (self.rlist[1] == 2) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r123") and ((self.rlist[0] == 1) and (self.rlist[1] == 3) and (self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r123") and ((self.rlist[0] == 2) and (self.rlist[1] == 1) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r123") and ((self.rlist[0] == 2) and (self.rlist[1] == 3) and (self.rlist[2] == 1)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r123") and ((self.rlist[0] == 3) and (self.rlist[1] == 1) and (self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r123") and ((self.rlist[0] == 3) and (self.rlist[1] == 2) and (self.rlist[2] == 1)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 2) and (self.rlist[1] == 3) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 2) and (self.rlist[1] == 4) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 3) and (self.rlist[1] == 2) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 3) and (self.rlist[1] == 4) and (self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 4) and (self.rlist[1] == 2) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r234") and ((self.rlist[0] == 4) and (self.rlist[1] == 3) and (self.rlist[2] == 2)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 3) and (self.rlist[1] == 4) and (self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 3) and (self.rlist[1] == 5) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 4) and (self.rlist[1] == 3) and (self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 4) and (self.rlist[1] == 5) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 5) and (self.rlist[1] == 3) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r345") and ((self.rlist[0] == 5) and (self.rlist[1] == 4) and (self.rlist[2] == 3)):
                    self.result = "win"
                    self.x = 36              
                elif (pressed == "r456") and ((self.rlist[0] == 4) and (self.rlist[1] == 5) and (self.rlist[2] == 6)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r456") and ((self.rlist[0] == 4) and (self.rlist[1] == 6) and (self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r456") and ((self.rlist[0] == 5) and (self.rlist[1] == 4) and (self.rlist[2] == 6)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r456") and ((self.rlist[0] == 5) and (self.rlist[1] == 6) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r456") and ((self.rlist[0] == 6) and (self.rlist[1] == 4) and (self.rlist[2] == 5)):
                    self.result = "win"
                    self.x = 36
                elif (pressed == "r456") and ((self.rlist[0] == 6) and (self.rlist[1] == 5) and (self.rlist[2] == 4)):
                    self.result = "win"
                    self.x = 36   
                elif (pressed == "Odd") and (self.rsum % 2) == 1:
                    self.result = "win"
                    self.x = 1
                elif (pressed == "Even") and (self.rsum % 2) == 0:
                    self.result = "win"
                    self.x = 1    
                else :
                    self.result = "lose"
                    self.x = 1

                if self.result == "win":
                    self.balance += self.x*(int(self.bet))
                elif self.result == "lose":
                    self.balance -= self.x*(int(self.bet))
                self.l_all.setText(str(self.balance))

                self.l_l.setText("0") 
                self.bet = 0
            else:
                self.l_l.setText("Error")
        else:
            self.l_all.setText("END")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi2(Form)
    Form.show()
    sys.exit(app.exec_())
