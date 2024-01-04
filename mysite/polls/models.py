from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
    # datetime.timedelta(days=1)表示一天的时间长度，这里是指pub_date在当前时间的一天之内


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey表示一对多的关系，on_delete=models.CASCADE表示级联删除
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
#Question.objects.filter(id=1) filter()函数返回一个QuerySet对象，包含满足条件的所有对象。
#Question.objects.filter(question_text__startswith="What") __startswith表示以什么开头
#Question.objects.get(pk=1) pk=primary key
#question.choice_set.all choice_set是Question模型的Choice模型的关系管理器的名称