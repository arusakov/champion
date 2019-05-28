from django.db import models


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
