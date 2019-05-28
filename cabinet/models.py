from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=255, unique=True)
    key = models.CharField(max_length=32, unique=True)


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Group(models.Model):
    COURSE_SDG = 'sdg' # Sports development group - группа спортивного совершенствования
    COURSE_TG = 'tg' # Training group - учебно-тренировочная группа
    COURSE_ITG1 = 'itg1' # 1st year initial training group - группа начальной подготовки 1-ого года
    COURSE_ITG2 = 'itg2' # Initial training group 2nd year - группа начальной подготовки 2-ого года
    COURSE_WG = 'wg' # Weekend group - группа выходного дня
    COURSE_CHOICES = (
        (COURSE_SDG, 'ГСС'),
        (COURSE_TG, 'УТГ'),
        (COURSE_ITG1, 'ГНП-1'),
        (COURSE_ITG2, 'ГНП-2'),
        (COURSE_WG, 'ГВД'),
    )

    course = models.CharField(choices=COURSE_CHOICES, max_length=16)


class Schedule(models.Model):
    DAY_MONDAY = 1
    DAY_TUESDAY = 2
    DAY_WEDNESDAY = 3
    DAY_THURSDAY = 4
    DAY_FRIDAY = 5
    DAY_SATURDAY = 6
    DAY_SUNDAY = 7
    DAY_CHOICES = (
        (DAY_MONDAY, 'Понедельник'),
        (DAY_TUESDAY, 'Вторник'),
        (DAY_WEDNESDAY, 'Среда'),
        (DAY_THURSDAY, 'Четверг'),
        (DAY_FRIDAY, 'Пятница'),
        (DAY_SATURDAY, 'Суббота'),
        (DAY_SUNDAY, 'Воскресение'),
    )

    week_day = models.PositiveSmallIntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    trainers = models.ManyToManyField(User)
