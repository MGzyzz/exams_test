import os
import django
from docx import Document

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tests_for_exams.models import Question, AnswerOption, Subject, CorrectAnswer

file_path = '../static/files/modified_тест_200_вопросов_по_философии.docx'  # Update the file path as necessary
subject = Subject.objects.get(name="Philosophy")  # Adjust the subject name as needed
doc = Document(file_path)

current_question = None
answer_options = []

for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('<question>'):
        # Process the previous question
        if current_question:
            current_question.save()
            for option in answer_options:
                option.save()

            # Reset for new question
            answer_options = []

        # New question
        question_text = text[len('<question>'):].strip()
        current_question = Question(text=question_text, subject=subject)
    elif text.startswith('<вариант>') and current_question is not None:
        # Add answer option
        option_text = text[len('<вариант>'):].strip()
        answer_option = AnswerOption(question=current_question, text=option_text)
        answer_options.append(answer_option)

# Process the last question
if current_question:
    current_question.save()
    for option in answer_options:
        option.save()


for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('<question>'):
        question_text = text[len('<question>'):].strip()
        # Найти соответствующий вопрос в базе данных
        current_question = Question.objects.filter(text=question_text).first()
    elif text.startswith('<вариант правильный>') and current_question is not None:
        # Найти соответствующий вариант ответа в базе данных
        correct_answer_text = text[len('<вариант правильный>'):].strip()
        correct_option = AnswerOption.objects.filter(question=current_question, text=correct_answer_text).first()
        if correct_option:
            # Создать запись о правильном ответе, если такая еще не существует
            CorrectAnswer.objects.get_or_create(question=current_question, answer=correct_option)