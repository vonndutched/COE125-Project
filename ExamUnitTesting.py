import unittest
from ExamBusinessLogic import Exam_BL

class TestLogin(unittest.TestCase):
    def testIsAnswerBlank(self):
        ebl = Exam_BL()
        self.assertEqual(ebl.IsAnswerBlank(""),True)
        self.assertEqual(ebl.IsAnswerBlank("Apple"),False)

    def testIsAnswerInChoices(self):
        ebl = Exam_BL()
        self.assertEqual(ebl.IsAnswerInChoices("Apple"),True)
        self.assertEqual(ebl.IsAnswerInChoices("DragonFruit"),False)
        
    def testIsAnswerCorrect(self):
        ebl = Exam_BL()
        ebl.SetCorrectAnswer("Apple")
        self.assertEqual(ebl.IsAnswerCorrect("Apple"),True)
        self.assertEqual(ebl.IsAnswerCorrect("Watermelon"),False)
        
    def testAddQuestionCurrent(self):
        ebl = Exam_BL()
        self.assertEqual(ebl.AddQuestionCurrent(),'2')
        self.assertEqual(ebl.AddQuestionCurrent(),'3')
        

if __name__ == "__main__":
    unittest.main()
        
    def AddScore(self):
        self.SetScore(self.GetScore() + 1)
        
    def RandomPictureInData(self):
        self.SetCorrectAnswer(self.ExamDL.RandomPicture())
        
    def AddQuestionCurrent(self):
        self.SetQuestionCurrent(self.GetQuestionCurrent() + 1)
        return str(self.GetQuestionCurrent())
        
        
    