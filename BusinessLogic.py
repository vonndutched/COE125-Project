from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from DataLogic import Data_Logic
from Register import Ui_MainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 523)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Login_Username = QtWidgets.QLineEdit(Dialog)
        self.Login_Username.setGeometry(QtCore.QRect(210, 190, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Login_Username.setFont(font)
        self.Login_Username.setObjectName("Login_Username")
        self.CreateAcc = QtWidgets.QPushButton(Dialog)
        self.CreateAcc.setGeometry(QtCore.QRect(90, 430, 141, 41))
        self.CreateAcc.setObjectName("CreateAcc")
        self.NextToPass = QtWidgets.QPushButton(Dialog)
        self.NextToPass.setGeometry(QtCore.QRect(240, 260, 171, 61))
        self.NextToPass.setObjectName("NextToPass")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 251, 17))
        self.label_2.setObjectName("label_2")
        
        self.NextToPass.clicked.connect(self.Login)
        self.CreateAcc.clicked.connect(self.GoToRegister)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.CreateAcc.setText(_translate("Dialog", "Register"))
        self.NextToPass.setText(_translate("Dialog", "Next"))
        self.label_2.setText(_translate("Dialog", "Don\'t have an account? Register now!"))

        global checkUser 
        global Username

        checkUser = False
        
    def Login(self): #This function check if the enter info is have account 
        
        global checkUser
        global Username
        
        if (checkUser == False):
            Username = self.Login_Username.text()
            if Username == "": #check if no input
                msg = QMessageBox()
                msg.setWindowTitle("System")
                msg.setText("Empty Username")
                msg.exec_()
                
            elif (Accounts.UserCheck(Username)):
                checkUser = True
                msg = QMessageBox()
                msg.setWindowTitle("System")
                msg.setText("USER FOUND")
                msg.exec_()
                self.label.setText("Password")
                self.Login_Username.setText("")
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("System")
                msg.setText("USER NOT FOUND")
                msg.exec_()
                
        elif (checkUser):
            Password = self.Login_Username.text()
            msg = QMessageBox()
            msg.setWindowTitle("System")
            Accounts.PasswordCheck(Username,Password)
            
            if (Accounts.PasswordCheck(Username,Password)):
                msg.setText("Password is correct!")
                message = Accounts.GetName(Username,Password)
                detail = ("The name of the user is " + message)
                msg.setDetailedText(detail)
                msg.exec_()  
                
            else:
                msg.setText("Password is incorrect!")
                msg.exec_() 
                
    def GoToRegister(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ai = Ui_MainWindow()
        self.ai.setupUi(self.MainWindow)
        self.MainWindow.show()
        Dialog.close()
                
                

if __name__ == "__main__":
    import sys
    Accounts = Data_Logic()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

