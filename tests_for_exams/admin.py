from django.contrib import admin
from tests_for_exams.models import AnswerOption, CorrectAnswer, Question, Subject, Test, UserAnswer
# Register your models here.


class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question')  # Поля, которые будут отображаться
    ordering = ('question', 'text')      # Сортировка ответов по вопросу и тексту
    list_filter = ('question',)          # Фильтры по вопросам
    search_fields = ('text',)            # Поиск по тексту ответа


class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('id',)


class CorrectAnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_filter = ('id',)


admin.site.register(AnswerOption, AnswerOptionAdmin)
admin.site.register(CorrectAnswer, CorrectAnswerOptionAdmin)
admin.site.register(Question, QuestionOptionAdmin)
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(UserAnswer)
