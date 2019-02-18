from django import forms

from promo.models import RequestInfo


class RequestForm(forms.ModelForm):
    agreement = forms.BooleanField()

    class Meta:
        model = RequestInfo
        fields = ('children_name', 'children_birthday', 'phone', 'email',
                  'name', 'comments', 'agreement')
