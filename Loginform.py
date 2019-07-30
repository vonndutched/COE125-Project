# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loginform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv #parang include whatever para gumana si csv.reader function


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
        self.Login_Username.setObjectName("Login_Username") #LINEDIT
        self.NextToPass = QtWidgets.QPushButton(Dialog) #Next before password
        self.NextToPass.setGeometry(QtCore.QRect(240, 260, 171, 61))
        self.NextToPass.setObjectName("NextToPass")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 400, 251, 17))
        self.label_2.setObjectName("label_2")


        self.NextToPass.clicked.connect(self.Login)
        #if self.label.Text == "Password":

        global Username
        global check
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.NextToPass.setText(_translate("Dialog", "Next"))
        global checkUser 
        global check
        global PasswordGet
        global FirstName
        global LastName
        checkUser = False
        check = False
        
    def Login(self):#This function check if the enter info is have account 
        
        global Username
        global checkUser
        global check
        global PasswordGet
        global FirstName
        global LastName
        
        if checkUser == False:
            Username = self.Login_Username.text()
        else:
            Password = self.Login_Username.text()
        
        
        if Username == "": #check if no input
            msg = QMessageBox()
            msg.setWindowTitle("System")
            msg.setText("Empty Username")
            msg.exec_()
            check = True
        
        elif checkUser == False:    
            with open('test.csv')as csv_file: #read ung csv file
                csv_reader = csv.reader(csv_file, delimiter=',')  #csv.reader comes from import csv
                line_count = 0 
              
                for row in csv_reader:
                    if line_count == 0: #para iskip yung first column
                        line_count += 1
                    elif line_count >= 1: #Sesearch buong column at first row for the user
                        if Username == row[0]:
                            msg = QMessageBox()
                            msg.setWindowTitle("System")
                            msg.setText("USER FOUND")
                            msg.exec_()
                            self.label.setText("Password")
                            self.Login_Username.setText("")
                            PasswordGet = row[1]
                            FirstName = row[2]
                            LastName = row[3]
                            check = True
                            checkUser = True
                            break
                        
        elif checkUser == True:
            if PasswordGet == Password:
                msg = QMessageBox()
                msg.setWindowTitle("System")
                #msg.setText("Password is correct!\n The name of the user", Username, "is", FirstName, LastName)
                msg.setText("Password is correct!")
                detail = ("The name of the user is ")
                msg.setDetailedText(detail + FirstName +" "+ LastName)
                msg.exec_()   #output first name last name
                check = True
            else:
                msg = QMessageBox()
                msg.setWindowTitle("System")
                msg.setText("Password is incorrect")
                msg.exec_()   #output first name last name
            

        if check == False:
            msg = QMessageBox()
            msg.setWindowTitle("System")
            msg.setText("User not found!")
            msg.exec_()   
            self.Login_Username.setText("")




 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


