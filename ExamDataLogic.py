import sqlite3

class Exam_DL:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()
        
    def RandomPicture(self):
        Image = self.cursor.execute("SELECT * FROM Images ORDER BY RANDOM () LIMIT 1")
        for x in Image:
            rec_data = x[1]
            ActualAnswer = x[2]
            
        with open('fruit.jpg', 'wb') as f:
            f.write(rec_data)
        self.connection.commit()
        return ActualAnswer
                    
    
