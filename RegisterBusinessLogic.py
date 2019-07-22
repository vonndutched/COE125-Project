from RegisterDataLogic import Register_DL

class Register_BL:
    def __init__(self):
        self.RegisterDL = Register_DL()
        self._Username = None
        self._Password = None
        self._FirstName = None
        self._LastName = None

########            SETTERS         #######################################################
        
    def SetUsername(self, username):
        self._Username = username
        
    def SetPassword(self, password):
        self._Password = password
        
    def SetFirstName(self, firstname):
        self._FirstName = firstname
        
    def SetLastName(self, lastname):
        self._LastName = lastname     
        
########            GETTERS         #######################################################
    
    def GetUsername(self):
        return self._Username
        
    def GetPassword(self):
        return self._Password
        
    def GetFirstName(self):
        return self._FirstName
        
    def GetLastName(self):
        return self._LastName
        
########            PROCESS        ########################################################        
    
    def AreFieldsBlank(self, username, password, firstname, lastname):
        if username == "" or password == "" or firstname == "" or lastname == "":
            return True
        else:
            return False
        
    def IsUsernameExistInData(self, username):
        if self.RegisterDL.RegisterUserCheck(username):
            return True
        else:
            return False
        
    def AddUserToData(self, username, password, firstname,lastname):
        self.RegisterDL.AddNewUser(username, password, firstname,lastname)


        


