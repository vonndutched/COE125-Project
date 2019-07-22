import sqlite3

class Register_DL:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row #enable fetchall
                    
    def RegisterUserCheck(self, username):
        self.cursor.execute("SELECT * FROM Users")
        AllRows = self.cursor.fetchall() # Gets the rows of all the columns
        for row in AllRows:
            if (str(row[0]) == username):
                self.connection.commit()
                return True
        self.connection.commit() #Equivalent to file.close
        return False
    
    def AddNewUser(self, username, password, firstname,lastname):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('Insert INTO Users(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME) VALUES(?,?,?,?)',(username,password,firstname,lastname))
        self.connection.commit()
        return True
    
