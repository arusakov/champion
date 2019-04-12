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

class FullNameMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

User = auth.get_user_model()
class LessonForm(forms.ModelForm):
    place = NameChoiceField(queryset=models.Place.objects.all())
    trainer = FullNameMultipleChoiceField(queryset=User.objects.filter(groups__name='trainer'))
    class Meta:
        model = models.Lesson
        fields = ('place','trainer','week_day','start_time','duration')
