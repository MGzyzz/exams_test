from django.db import models
from core import settings
from tests_for_exams.models import Question, AnswerOption

class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} - {self.question.text} - {self.selected_answer.text}'
