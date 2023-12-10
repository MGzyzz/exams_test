import os
import django
from docx import Document

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tests_for_exams.models import Question, AnswerOption, Subject

# Путь к файлу
file_path = '../static/files/тест 104 вопросов.docx'

subject = Subject.objects.get(name="Philosophy")

# Открытие документа Word
doc = Document(file_path)

current_question = None
answer_options = []

for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('<question>'):
        # Сохраняем предыдущий вопрос и его ответы
        if current_question:
            current_question.save()
            AnswerOption.objects.bulk_create(answer_options)
            answer_options = []

        # Создание нового вопроса
        question_text = text[len('<question>'):].strip()
        current_question = Question(text=question_text, subject=subject)
    elif text.startswith('<вариант>') and current_question is not None:
        # Добавление варианта ответа
        option_text = text[len('<вариант>'):].strip()
        answer_options.append(AnswerOption(question=current_question, text=option_text))

# Не забываем сохранить последний вопрос и его ответы
if current_question and answer_options:
    current_question.save()
    AnswerOption.objects.bulk_create(answer_options)
