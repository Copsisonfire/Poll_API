from rest_framework import generics
from django.utils.timezone import now
from poll_api.models import (Poll,
                             Question,
                             UserAnswer,
                             )
from poll_api.serializers import (PollSerializer,
                                  QuestionSerializer,
                                  UserAnswerSerializer,
                                  AnsweredSerializer,
                                  )
from rest_framework.permissions import IsAdminUser
from django.shortcuts import (get_object_or_404,
                              get_list_or_404)


class PollListView(generics.ListAPIView):
    """Показывает только активные опросы"""
    serializer_class = PollSerializer
    queryset = Poll.objects.filter(end_date__gt=now())

class PollCreateView(generics.CreateAPIView):
    """Для создания опросов. Только для админа"""
    serializer_class = PollSerializer
    permission_classes = (IsAdminUser, )

class PollEditView(generics.RetrieveUpdateAPIView):
    """Для редактирования опросов. Только для админа"""
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAdminUser,)

class PollDeleteView(generics.RetrieveDestroyAPIView):
    """Для удаления опросов. Только для админа"""
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAdminUser, )

class QuestionCreateView(generics.CreateAPIView):
    """Для создания вопросов. Только для админа"""
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )

class QuestionEditView(generics.RetrieveUpdateAPIView):
    """Для редактирования вопросов. Только для админа"""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAdminUser, )

class QuestionDeleteView(generics.RetrieveDestroyAPIView):
    """Для удаления вопросов. Только для админа"""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAdminUser, )

class QuestionListView(generics.ListAPIView):
    """Показывает вопросы для заданного id опроса. Проверяет, активен ли
    опрос"""
    serializer_class = QuestionSerializer
    def get_queryset(self):
        poll_number = self.request.query_params.get('poll_id')
        poll_obj = get_object_or_404(Poll, id=poll_number)
        if poll_obj.end_date >= now().date():
            return get_list_or_404(Question, poll_id=poll_number)

class UserAnswerCreateView(generics.CreateAPIView):
    """Создаёт ответ пользователя"""
    serializer_class = UserAnswerSerializer
    queryset = UserAnswer

class UserAnswerDetailView(generics.ListAPIView):
    """Показывает ответы пользователя"""
    serializer_class = AnsweredSerializer
    def get_queryset(self):
            return get_list_or_404(UserAnswer, user=self.kwargs['user'])





