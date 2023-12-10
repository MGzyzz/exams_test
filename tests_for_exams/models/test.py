from django.db import models
from tests_for_exams.models import Question


class Test(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name