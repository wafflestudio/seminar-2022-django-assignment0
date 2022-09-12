import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# 모델은 데이터에 대한 단 하나의 확실한 정보 출처
# 저장중인 데이터의 필수 필드 및 동작이 포함됨
# 목표는 데이터 모델을 한 곳에서 정의 후 데이터 모델을 자동으로 파생하는 것(migrate가 여기 포함됨.)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# FOREGIN KEY를 통해 여러 개의 choice가 각 하나의 question에 대응됨을 보여줌.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 모델의 변경을 만드는 순서는
# 1. models.py에서 모델을 변경한 후
# 2. python manage.py makemigrations을 통해 변경사항에 대한 마이그레이션을 만들고
# 3. python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용