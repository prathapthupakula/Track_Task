from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

yesorno = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

# Create your models here.
class TrackData(models.Model):
    track_name=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = 'Track Data'
    def __str__(self):
        return self.track_name
class QuestionData(models.Model):
    track = models.ForeignKey(TrackData, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    class Meta:
        # managed = False
        # db_table = 'newapp_questiondata'
        # verbose_name = 'Question Data'
        verbose_name_plural = 'Question Data'

    def __str__(self):
        return self.question_text
class ChoiceData(models.Model):
    question = models.ForeignKey(QuestionData, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_it_right = models.CharField(max_length=10, choices=yesorno,default="N")
    votes = models.IntegerField(default=0)

    class Meta:
        # managed = False
        # verbose_name = 'Choice'
        verbose_name_plural = 'Choice Data'
    def __str__(self):
        return self.choice_text


