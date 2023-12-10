import random

from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from tests_for_exams.models import Question, AnswerOption, CorrectAnswer, Test, UserAnswer


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = Test.objects.all()
        return context


class QuestionListView(ListView):
    model = Question
    template_name = 'questions_list.html'
    context_object_name = 'questions'
    paginate_by = 10

    def post(self, request):
        for key, value in request.POST.items():
            if key.startswith('correct_answer_'):
                question_id = key.split('_')[-1]
                answer_id = value
                question = Question.objects.get(id=question_id)
                answer = AnswerOption.objects.get(id=answer_id)

                CorrectAnswer.objects.update_or_create(question=question, defaults={'answer': answer})
                messages.success(request, "Ответы обновлены.")

        return redirect('questions_list')


class GenerateTestView(View):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.order_by('?')[:30]
        test = Test.objects.create(name="Психология Test {}".format(Test.objects.count() + 1))
        test.questions.add(*questions)
        return redirect('home')


class TestDetailView(DetailView):
    model = Test
    template_name = 'test_detail.html'
    context_object_name = 'test'


class SubmitTestView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                selected_answer_id = value
                UserAnswer.objects.create(
                    user=user,
                    question_id=question_id,
                    selected_answer_id=selected_answer_id
                )
        test_id = self.kwargs.get('test_id')
        return redirect('test_result', test_id=test_id)


class TestResultView(TemplateView):
    template_name = 'test_result.html'

    def get_context_data(self, **kwargs):
        context = super(TestResultView, self).get_context_data(**kwargs)
        test_id = self.kwargs['test_id']
        user_answers = UserAnswer.objects.filter(user=self.request.user, question__test=test_id)

        total_questions = Test.objects.get(id=test_id).questions.count()
        correct_answers_count = 0

        questions_with_answers = []
        for user_answer in user_answers:
            correct_answer = CorrectAnswer.objects.get(question=user_answer.question)
            is_correct = user_answer.selected_answer == correct_answer.answer
            if is_correct:
                correct_answers_count += 1

            questions_with_answers.append({
                'question': user_answer.question,
                'selected_answer': user_answer.selected_answer,
                'correct_answer': correct_answer.answer,
                'is_correct': is_correct,
            })

        context['total_questions'] = total_questions
        context['correct_answers_count'] = correct_answers_count
        context['questions_with_answers'] = questions_with_answers
        return context
