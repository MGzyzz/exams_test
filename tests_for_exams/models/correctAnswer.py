from django.db import models
from tests_for_exams.models.question import Question
from tests_for_exams.models.answerOption import AnswerOption


class CorrectAnswer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.text}: Correct {self.answer.text}'