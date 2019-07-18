from PyQt5 import QtCore, QtGui, QtWidgets
from DataLogic import Data_Logic
from RegisterBusinessLogic import Ui_RegisterWindow
from ExamBusinessLogic import Ui_ExamWindow
from PyQt5 import QtTest


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(244, 252)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        LoginWindow.setPalette(palette)
        self.Label_Username = QtWidgets.QLabel(LoginWindow)
        self.Label_Username.setGeometry(QtCore.QRect(10, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Username.setFont(font)
        self.Label_Username.setObjectName("Label_Username")
        self.lineEdit_Username = QtWidgets.QLineEdit(LoginWindow)
        self.lineEdit_Username.setGeometry(QtCore.QRect(102, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Username.setFont(font)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.pushButton_SignIn = QtWidgets.QPushButton(LoginWindow)
        self.pushButton_SignIn.setGeometry(QtCore.QRect(110, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SignIn.setFont(font)
        self.pushButton_SignIn.setObjectName("pushButton_SignIn")
        self.Label_SignIn1 = QtWidgets.QLabel(LoginWindow)
        self.Label_SignIn1.setGeometry(QtCore.QRect(100, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_SignIn1.setFont(font)
        self.Label_SignIn1.setObjectName("Label_SignIn1")
        self.Label_SignIn2 = QtWidgets.QLabel(LoginWindow)
        self.Label_SignIn2.setGeometry(QtCore.QRect(60, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_SignIn2.setFont(font)
        self.Label_SignIn2.setObjectName("Label_SignIn2")
        self.Label_CreateAcc = QtWidgets.QLabel(LoginWindow)
        self.Label_CreateAcc.setGeometry(QtCore.QRect(10, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_CreateAcc.setFont(font)
        self.Label_CreateAcc.setObjectName("Label_CreateAcc")
        self.pushButton_CreateAcc = QtWidgets.QPushButton(LoginWindow)
        self.pushButton_CreateAcc.setGeometry(QtCore.QRect(40, 210, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CreateAcc.setFont(font)
        self.pushButton_CreateAcc.setObjectName("pushButton_CreateAcc")
        self.pushButton_Exit = QtWidgets.QPushButton(LoginWindow)
        self.pushButton_Exit.setGeometry(QtCore.QRect(180, 220, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.Label_StatusSignIn = QtWidgets.QLabel(LoginWindow)
        self.Label_StatusSignIn.setGeometry(QtCore.QRect(10, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_StatusSignIn.setFont(font)
        self.Label_StatusSignIn.setObjectName("Label_StatusSignIn")
        
        self.pushButton_SignIn.clicked.connect(self.SignIn)
        self.pushButton_CreateAcc.clicked.connect(self.GoToRegisterWin)
        self.pushButton_Exit.clicked.connect(self.CloseProgram)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.Label_Username.setText(_translate("LoginWindow", "Username:"))
        self.pushButton_SignIn.setText(_translate("LoginWindow", "Next"))
        self.Label_SignIn1.setText(_translate("LoginWindow", "Sign In"))
        self.Label_SignIn2.setText(_translate("LoginWindow", "Using Your Account"))
        self.Label_CreateAcc.setText(_translate("LoginWindow", "Don\'t Have An Account?"))
        self.pushButton_CreateAcc.setText(_translate("LoginWindow", "Create Account"))
        self.pushButton_Exit.setText(_translate("LoginWindow", "Exit"))
        self.Label_StatusSignIn.setText(_translate("LoginWindow", "Status"))
        self.Label_StatusSignIn.hide()
        
        global checkUser 
        global Username

        checkUser = False
        
    def SignIn(self): #This function check if the enter info is have account 
        self.Label_StatusSignIn.show()
        
        
        global checkUser
        global Username
        
        if (checkUser == False):
            Username = self.lineEdit_Username.text()
            if Username == "": #check if no input
                self.Label_StatusSignIn.setStyleSheet("color: red;")
                self.Label_StatusSignIn.setText("Empty Username!")
                
            elif (Accounts.UserCheck(Username)):
                checkUser = True
                self.Label_StatusSignIn.setStyleSheet("color: green;")
                self.Label_StatusSignIn.setText("User Found!")
                self.Label_Username.setText("Password:")
                self.lineEdit_Username.setText("")
                
            else:
                self.Label_StatusSignIn.setStyleSheet("color: red;")
                self.Label_StatusSignIn.setText("User Not Found!")
                
        elif (checkUser):
            Password = self.lineEdit_Username.text()
            
            if Password == "":
                self.Label_StatusSignIn.setStyleSheet("color: red;")
                self.Label_StatusSignIn.setText("Empty Password!")
                
            else:    
                if (Accounts.PasswordCheck(Password)):
                    self.Label_StatusSignIn.setStyleSheet("color: green;")
                    self.Label_StatusSignIn.setText("Password is correct!\nWelcome " 
                                                    + Accounts.GetName(Password) + "!")
                    
                    QtTest.QTest.qWait(3000)
                    self.ExamWindow = QtWidgets.QMainWindow()
                    self.ei = Ui_ExamWindow()
                    self.ei.setupUi(self.ExamWindow)
                    self.ExamWindow.show()
                    LoginWindow.close()
                    
                else:
                    self.Label_StatusSignIn.setStyleSheet("color: red;")
                    self.Label_StatusSignIn.setText("Password is incorrect!")
                
    def GoToRegisterWin(self):
        self.RegisterWindow = QtWidgets.QMainWindow()
        self.ri = Ui_RegisterWindow()
        self.ri.setupUi(self.RegisterWindow)
        self.RegisterWindow.show()
        
        #LoginWindow.hide()
    
    def CloseProgram(self):
        self.Label_StatusSignIn.setStyleSheet("color: green;")
        self.Label_StatusSignIn.setText("Thank you for using our application!")
        QtTest.QTest.qWait(3000)

        LoginWindow.close()


if __name__ == "__main__":
    import sys
    Accounts = Data_Logic()
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

