from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)

class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

class Place(models.Model):
    name = models.CharField(max_length=255)

class Lesson(models.Model):
    WEEK_DAY_CHOICES = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    trainer = models.ManyToManyField(User)
    week_day = models.SmallIntegerField(choices=WEEK_DAY_CHOICES)
    start_time = models.TimeField()
    duration = models.DurationField()
