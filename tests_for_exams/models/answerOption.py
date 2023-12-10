from django.db import models
from tests_for_exams.models.question import Question


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_options')
    text = models.TextField()

    def __str__(self):
        return self.text