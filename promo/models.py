from django.db import models


class RequestInfo(models.Model):
    children_name = models.CharField(max_length=255)
    children_birthday = models.DateField()
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    comments = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
