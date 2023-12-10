import os
import django
from docx import Document

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tests_for_exams.models import Question, AnswerOption, Subject  # Импортируйте ваши модели

# Путь к файлу
file_path = '../static/files/тест 104 вопросов.docx'

subject = Subject.objects.get(name="Psychology")

# Открытие документа Word
doc = Document(file_path)

current_question = None

for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('вопрос'):
        # Создание нового вопроса
        question_text = text[len('вопрос'):].strip()
        current_question = Question(text=question_text, subject=subject)
        current_question.save()
    elif text.startswith('вариант') and current_question is not None:
        # Добавление варианта ответа к текущему вопросу
        answer_text = text[len('вариант'):].strip()
        AnswerOption(question=current_question, text=answer_text).save()
