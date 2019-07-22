from ExamDataLogic import Exam_DL

class Exam_BL:
    def __init__(self):
        self.ExamDL = Exam_DL()
        self._Score = 0
        self._ImagePath = None
        self._Answer = None
        self._CorrectAnswer = None
        self._IsAnswerCorrect = False
        self._QuestionCurrent = 1

########            SETTERS         #######################################################
        
    def SetScore(self, score):
        self._Score = score
        
    def SetImagePath(self, imagepath):
        self._ImagePath = imagepath
        
    def SetAnswer(self, answer):
        self._Answer = answer
        
    def SetCorrectAnswer(self, correctanswer):
        self._CorrectAnswer = correctanswer  
        
    def SetIsAnswerCorrect(self, isanswercorrect):
        self._IsAnswerCorrect = isanswercorrect
        
    def SetQuestionCurrent(self, questioncurrent):
        self._QuestionCurrent = questioncurrent
        
########            GETTERS         #######################################################
    
    def GetScore(self):
        return self._Score
        
    def GetImagePath(self):
        return self._ImagePath
        
    def GetAnswer(self):
        return self._Answer
        
    def GetCorrectAnswer(self):
        return self._CorrectAnswer

    def GetIsAnswerCorrect(self):
        return self._IsAnswerCorrect
    
    def GetQuestionCurrent(self):
        return self._QuestionCurrent
    
########            PROCESS        ########################################################        
    
    def IsAnswerBlank(self, answer):
        if answer == "":
            return True
        else:
            return False
    
    def IsAnswerInChoices(self, answer):
        if answer == "Banana" or answer == "Apple" or answer == "Grape" or answer == "Orange" or answer == "Mango" or answer == "Watermelon":
                return True
        else:
            return False
        
    def IsAnswerCorrect(self, answer):
        if answer == self.GetCorrectAnswer():
            return True
        else:
            return False
        
    def AddScore(self):
        self.SetScore(self.GetScore() + 1)
        
    def RandomPictureInData(self):
        self.SetCorrectAnswer(self.ExamDL.RandomPicture())
        
    def AddQuestionCurrent(self):
        self.SetQuestionCurrent(self.GetQuestionCurrent() + 1)
        return str(self.GetQuestionCurrent())
    



        


