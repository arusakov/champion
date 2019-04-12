from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)

class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

class Place(models.Model):
    name = models.CharField(max_length=255)

class Lesson(models.Model):
    WEEK_DAY_CHOICES = enumerate(('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'))

    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    trainer = models.ManyToManyField(User, related_name='lessons')
    week_day = models.SmallIntegerField(choices=WEEK_DAY_CHOICES)
    start_time = models.TimeField()
    duration = models.DurationField()
