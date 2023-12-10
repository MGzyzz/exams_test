import os
import django
from docx import Document

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tests_for_exams.models import Question, AnswerOption, Subject, CorrectAnswer

file_path = '../static/files/1.docx'

subject = Subject.objects.get(name="robot")

doc = Document(file_path)

current_question = None
answer_options = []
answer_right = []

for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('<question>'):
        if current_question:
            current_question.save()
            for option in answer_options:
                option.save()
                if option.text in answer_right:
                    CorrectAnswer.objects.create(question=current_question, answer=option)
            answer_options = []
            answer_right = []

        question_text = text[len('<question>'):].strip()
        current_question = Question(text=question_text, subject=subject)
    elif text.startswith('<variant>') and current_question is not None:
        option_text = text[len('<variant>'):].strip()
        answer_options.append(AnswerOption(question=current_question, text=option_text))
    elif text.startswith('<variantright>') and current_question is not None:
        answer_right.append(text[len('<variantright>'):].strip())

if current_question:
    current_question.save()
    for option in answer_options:
        option.save()
        if option.text in answer_right:
            CorrectAnswer.objects.create(question=current_question, answer=option)