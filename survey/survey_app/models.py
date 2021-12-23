from django.db import models
from multiselectfield import MultiSelectField
from django.db.models import When
import datetime
from django.contrib.auth import get_user_model


class Survey(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'


        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE')
        )


    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    type = models.CharField(
        max_length=11, choices=Type.choices, default=Type.TEXT
    )
    # choice_option = (('Choice1, Choice1'), ('Choice2, Choice2'), ('Choice3, Choice3'))
    # multichoice = MultiSelectField(choices = choice_option)
    # choices = models.CharField(max_length=300, choices=Type.choices)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    variant = models.CharField(max_length=64, default='Enter value')

    def __str__(self):
        return self.variant


class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    one_choice = models.ForeignKey(Choice, null=True, on_delete=models.CASCADE)
    many_choice = models.ManyToManyField(Choice, null=True)
    text = models.TextField(null=True)