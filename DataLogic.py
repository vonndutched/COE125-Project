import sqlite3

class Data_Logic:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row #enable fetchall
        self.User = None
        
    def UserCheck(self,Username):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall() # Gets the rows of all the columns
        for row in AllRows:
            if (str(row[0]) == Username):
                self.User = str(row[0])
                self.connection.commit() #Equivalent to file.close
                return True
        self.connection.commit() #Equivalent to file.close
        return False
    
    def PasswordCheck(self,Password):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall()
        #Message = "Incorrect Password"
        for row in AllRows:
            if (str(row[0]) == self.User):
                if(str(row[1]) == Password):
                    #Message = str(row[2] + " " + row[3])
                    self.connection.commit()
                    return True
        self.connection.commit()
        return False
    
    def GetName(self,Password):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall()
        Message = ""
        for row in AllRows:
            if (str(row[0]) == self.User):
                if(str(row[1]) == Password):
                    Message = str(row[2]) + " " + str(row[3])
                    self.connection.commit()
                    return Message
                else:
                    self.connection.commit()
                    return Message
    
    
    def AddUser(self,Username,Password,First_Name,Last_Name):
        self.cursor.execute('Insert INTO Users(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME) VALUES(?,?,?,?)',(Username,Password,First_Name,Last_Name))
        self.connection.commit()
        Message = "Added New User!"
        return Message
    
