from rest_framework import serializers
from poll_api.models import Poll, Question, UserAnswer


class QuestionSerializer(serializers.ModelSerializer):
    poll_id = serializers.PrimaryKeyRelatedField(queryset=Poll.objects)
    class Meta:
        model = Question
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class UserAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects)
    class Meta:
        model = UserAnswer
        fields = ['user', 'question', 'answer']

class AnsweredSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    class Meta:
        model = UserAnswer
        fields = ['user', 'question', 'answer']

