from django.db import models
from tests_for_exams.models.question import Question


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()