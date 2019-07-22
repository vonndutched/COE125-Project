from LoginDataLogic import Login_DL

class Login_BL:
    def __init__(self):
        self.LoginDL = Login_DL()
        self._Username = None
        self._Password = None
        self._FirstName = None
        self._LastName = None
        self._UserExist = False
        self._UserMatch = False
        
########            SETTERS         #######################################################
        
    def SetUsername(self, username):
        self._Username = username
        
    def SetPassword(self, password):
        self._Password = password
        
    def SetFirstName(self, firstname):
        self._FirstName = firstname
        
    def SetLastName(self, lastname):
        self._LastName = lastname
        
    def SetUserExist(self, userexist):
        self._UserExist = userexist
        
    def SetUserMatch(self, usermatch):
        self._UserMatch = usermatch
        
########            GETTERS         #######################################################
    
    def GetUsername(self):
        return self._Username
        
    def GetPassword(self):
        return self._Password
        
    def GetFirstName(self):
        return self._FirstName
        
    def GetLastName(self):
        return self._LastName
        
    def GetUserExist(self):
        return self._UserExist
    
    def GetUserMatch(self):
        return self._UserMatch
        
########            PROCESS        ########################################################        
    
    def IsUsernameBlank(self, username):
        if username == "":
            return True
        else:
            return False
        
    def IsUsernameInData(self, username):
        if self.LoginDL.LoginUserCheck(username):
            self.SetUserMatch(True)
            return True
        else:
            return False
        
    def IsPasswordBlank(self, password):
        if password == "":
            return True
        else:
            return False
        
    def IsPasswordInData(self, password):
        if self.GetUserMatch():
            if self.LoginDL.PasswordCheck(password):
                self.SetFirstName(self.LoginDL.GetFirstNameData(password))
                self.SetLastName(self.LoginDL.GetLastNameData(password))
                return True
            else:
                return False
        return False

