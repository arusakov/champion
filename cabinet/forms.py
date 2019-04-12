from django import forms
from django.contrib import auth

from cabinet import models

class NameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class GroupForm(forms.ModelForm):
    course = NameChoiceField(queryset=models.Course.objects.all())
    class Meta:
        model = models.Group
        fields = ('course',)

class FullNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

User = auth.get_user_model()
class LessonForm(forms.ModelForm):
    place = NameChoiceField(queryset=models.Place.objects.all())
    trainer = FullNameChoiceField(queryset=User.objects.filter(groups__name='trainer'))
    class Meta:
        model = models.Lesson
        fields = ('place','trainer','week_day','start_time','duration')
