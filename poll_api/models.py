from django.db import models


class Poll(models.Model):
    """Опросники"""
    name = models.CharField(max_length=200, verbose_name='Название',
                            unique=True)
    start_date = models.DateField(auto_now_add=True,
                                      verbose_name='Дата старта',
                                      editable=False)
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.CharField(max_length=200,
                                   verbose_name='Описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросники'
        ordering = ['-start_date', 'name']


class Question(models.Model):
    """Вопросы"""
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE,
                                verbose_name='Название опросника',
                                related_name='poll_id')
    text_q = models.CharField(max_length=200, verbose_name='Текст вопроса')
    question_type = [
        ('text_input', 'Ввод текста'),
        ('simple_choice', 'выбор одного ответа'),
        ('multi_choice', 'мультивыбор'),
    ]
    type_q = models.CharField(max_length=20, verbose_name='Тип ответа',
                              choices=question_type)
    def __str__(self):
        return f'Опросник: "{self.poll_id}", вопрос: "{self.text_q}"'
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class UserAnswer(models.Model):
    """Ответы юзеров"""
    user = models.IntegerField(default="0")
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='question')
    answer = models.CharField(max_length=200)
    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name = 'Ответ юзеров'
        verbose_name_plural = 'Ответы юзеров'