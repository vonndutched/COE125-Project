import unittest
from LoginBusinessLogic import Login_BL


class TestLogin(unittest.TestCase):
    def testLoginUserBlank(self):
        bl = Login_BL()
        self.assertEqual(bl.IsUsernameBlank(""),True)
        self.assertEqual(bl.IsUsernameBlank("wew"),False)
    
    def testLoginUserInData(self):
        bl = Login_BL()
        self.assertEqual(bl.IsUsernameInData("bits"),True)
        self.assertEqual(bl.IsUsernameInData("sweet"),True)
        self.assertEqual(bl.IsUsernameInData("wewewew"),False)
        
        self.assertTrue(bl.IsUsernameInData("bits"))
    
    def testPasswordBlank(self):
        bl = Login_BL()
        self.assertEqual(bl.IsPasswordBlank(""),True)
        self.assertEqual(bl.IsPasswordBlank("toyo"),False)
        
    def testPasswordInData(self):
        bl = Login_BL()
        bl.SetUsername("bits")
        bl.IsUsernameInData("bits")
        self.assertEqual(bl.IsPasswordInData("kang123"),True)
        self.assertEqual(bl.IsPasswordInData("malipass"),False)

if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
    