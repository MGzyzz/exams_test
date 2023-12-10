from django.db import models
from tests_for_exams.models.subject import Subject


class Question(models.Model):
    text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='questions_images/', blank=True, null=True)

    def __str__(self):
        return self.text