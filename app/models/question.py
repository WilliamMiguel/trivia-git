from flask_login import UserMixin

class Question(UserMixin):
    def __init__(self, question, option1, option2, option3, option4, answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer

    def to_json(self):
        return {
            'Pregunta': self.question,
            'Alternativas':[
                self.option1,
                self.option2,
                self.option3,
                self.option4
            ],
            'Respuesta': self.answer
        }