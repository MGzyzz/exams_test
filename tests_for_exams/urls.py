from django.contrib import admin
from django.urls import path
from tests_for_exams.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_answer', QuestionListView.as_view(), name='questions_list'),
    path('generate/', GenerateTestView.as_view(), name='generate_questions'),
    path('generate_philosophy_test/', GeneratePhilosophyTestView.as_view(), name='generate_philosophy_questions'),
    path('generate_ipc_test/', GenerateIPCTestView.as_view(), name='generate_ipc'),
    path('test/<int:pk>/', TestDetailView.as_view(), name='test_detail'),
    path('test_result/<int:test_id>/', TestResultView.as_view(), name='test_result'),
    path('submit_test/<int:test_id>/', SubmitTestView.as_view(), name='submit_test'),
    path('generate_docx/<int:test_id>/', generate_docx, name='generate_docx'),
    path('answer_docx', generate_docx_with_correct_answers_by_subject, name='answer_docx'),
    path('answer_docx_and_questions/', generate_docx_with_questions_and_answers, name='question_and_answer'),
]
