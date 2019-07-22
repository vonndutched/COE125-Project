import sqlite3

class Login_DL:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row #enable fetchall
        self.User = None
        
    def LoginUserCheck(self,Username):
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
        for row in AllRows:
            if (str(row[0]) == self.User):
                if(str(row[1]) == Password):
                    self.connection.commit()
                    return True
        self.connection.commit()
        return False
    
    def GetFirstNameData(self,Password):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall()
        Message = ""
        for row in AllRows:
            if (str(row[0]) == self.User):
                if(str(row[1]) == Password):
                    Message = str(row[2])
                    self.connection.commit()
                    return Message
                else:
                    self.connection.commit()
                    return Message
                
    def GetLastNameData(self,Password):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall()
        Message = ""
        for row in AllRows:
            if (str(row[0]) == self.User):
                if(str(row[1]) == Password):
                    Message = str(row[3])
                    self.connection.commit()
                    return Message
                else:
                    self.connection.commit()
                    return Message
    
