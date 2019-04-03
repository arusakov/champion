from django import forms

from cabinet import models

class NameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class GroupForm(forms.ModelForm):
    course = NameChoiceField(queryset=models.Course.objects.all())
    class Meta:
        model = models.Group
        fields = ('course',)

class LessonForm(forms.ModelForm):
    place = NameChoiceField(queryset=models.Place.objects.all())
    class Meta:
        model = models.Lesson
        fields = ('place','trainer','week_day','start_time','duration')
