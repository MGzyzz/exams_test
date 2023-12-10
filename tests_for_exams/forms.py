from django import forms
from .models import Question, AnswerOption, CorrectAnswer, Subject


class QuestionForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = Question
    #     fields = ['text', 'subject', 'image']  # Указывайте поля, которые вы хотите включить в форму
    #     widgets = {
    #         'text': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
    #         'subject': forms.Select(),
    #         'image': forms.FileInput()
    #     }
    #
    # def __init__(self, *args, **kwargs):
    #     super(QuestionForm, self).__init__(*args, **kwargs)
    #     self.fields['subject'].queryset = Subject.objects.all()