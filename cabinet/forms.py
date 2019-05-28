from django import forms

from cabinet.models import Group


class GroupForm(forms.Form):
    course = forms.ChoiceField(choices=Group.COURSE_CHOICES, label='Направление')
