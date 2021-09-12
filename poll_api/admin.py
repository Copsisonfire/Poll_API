from django.contrib import admin

from .models import (Poll,
                     Question,
                     UserAnswer
                     )


class PollAdmin(admin.ModelAdmin):
    """Опросники"""
    list_display = ('id', 'name', 'description', 'start_date', 'end_date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class QuestionAdmin(admin.ModelAdmin):
    """Вопросы"""
    list_display = ('id', 'text_q', 'type_q', 'poll_id')
    list_display_links = ('id', )

class UserAnswerAdmin(admin.ModelAdmin):
    """Ответы"""
    list_display = ('id', 'user', 'answer', 'question')
    list_display_links = ('question', )

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)