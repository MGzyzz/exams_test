import os
import django
from docx import Document

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tests_for_exams.models import Question, AnswerOption, Subject, CorrectAnswer

file_path = '../static/files/IPC_final_1_word_format.docx'
subject = Subject.objects.get(name="IPC")
doc = Document(file_path)

current_question = None
answer_options = []

for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('<question>'):
        if current_question:
            current_question.save()
            for option in answer_options:
                option.save()
            answer_options = []

        question_text = text[len('<question>'):].strip()
        current_question = Question(text=question_text, subject=subject)
    elif text.startswith('<variant>') and current_question:
        option_text = text[len('<variant>'):].strip()
        answer_option = AnswerOption(question=current_question, text=option_text)
        answer_options.append(answer_option)
    elif text.startswith('<variantright>') and current_question:
        if not current_question.pk:
            current_question.save()
            for option in answer_options:
                option.save()
            answer_options = []

        correct_answer_text = text[len('<variantright>'):].strip()
        correct_option = AnswerOption(question=current_question, text=correct_answer_text)
        CorrectAnswer.objects.get_or_create(question=current_question, answer=correct_option)

if current_question:
    current_question.save()
    for option in answer_options:
        option.save()

