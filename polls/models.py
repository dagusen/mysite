import datetime
from django.db import models
<<<<<<< HEAD
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
=======
from django.utils.encoding import datetime from django.utils import time zone
>>>>>>> 6808b972767adbcfaa7adb7806dde2b4031aca45
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
<<<<<<< HEAD
    	return self.question_text
=======
        return self.question_text
>>>>>>> 6808b972767adbcfaa7adb7806dde2b4031aca45
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text