from django.urls import path
from poll_api.views import (PollListView,
                            PollCreateView,
                            PollEditView,
                            PollDeleteView,
                            QuestionCreateView,
                            QuestionEditView,
                            QuestionDeleteView,
                            QuestionListView,
                            UserAnswerCreateView,
                            UserAnswerDetailView,
                            )

urlpatterns = [
    path('active_polls/', PollListView.as_view()),   #Активные опросы
    path('poll/create/', PollCreateView.as_view()),   #Созд. опросов
    path('poll/edit/<int:id>/', PollEditView.as_view()),   #Ред. опроса
    path('poll/delete/<int:id>/', PollDeleteView.as_view()),   #Удал. опроса
    path('question/create/', QuestionCreateView.as_view()),   #Созд. вопроса
    path('question/edit/<int:id>/', QuestionEditView.as_view()),   #Ред. вопрос
    path('question/delete/<int:id>/', QuestionDeleteView.as_view()), #Удал. воп
    path('active_polls/poll/', QuestionListView.as_view()),  #Показать вопросы
# по Poll_id в query_params. ?poll_id=номер опроса
    path('active_polls/poll/answer/', UserAnswerCreateView.as_view()),   #Ответ
    path('my_answers/<int:user>/', UserAnswerDetailView.as_view()),   #Показ
#всех ответов по id_user
    ]