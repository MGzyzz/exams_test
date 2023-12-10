from django.contrib import admin
from django.urls import path
from tests_for_exams.views import QuestionListView, Home, GenerateTestView, TestDetailView, TestResultView, SubmitTestView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_answer', QuestionListView.as_view(), name='questions_list'),
    path('generate/', GenerateTestView.as_view(), name='generate_questions'),
    path('test/<int:pk>/', TestDetailView.as_view(), name='test_detail'),
    path('test_result/<int:test_id>/', TestResultView.as_view(), name='test_result'),
    path('submit_test/<int:test_id>/', SubmitTestView.as_view(), name='submit_test'),
]
