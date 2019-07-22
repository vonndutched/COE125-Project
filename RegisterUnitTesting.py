import unittest
from RegisterBusinessLogic import Register_BL

class TestLogin(unittest.TestCase):
    def testAreFieldsBLank(self):
        rbl = Register_BL()
        self.assertEqual(rbl.AreFieldsBlank("","","",""),True)
        self.assertEqual(rbl.AreFieldsBlank("wew","","kwek",""),True)
        self.assertEqual(rbl.AreFieldsBlank("AnnouncerEasy","ypWdQgUV","Angie","Mcghee"),False)
    
    def testRegUserExistInData(self):
        rbl = Register_BL()
        self.assertEqual(rbl.IsUsernameExistInData("bits"),True)
        self.assertEqual(rbl.IsUsernameExistInData("sweet"),True)
        self.assertEqual(rbl.IsUsernameExistInData("wewewew"),False)
        
        self.assertTrue(rbl.IsUsernameExistInData("ChampPool"))

if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
    