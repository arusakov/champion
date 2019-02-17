from django import forms

class OrderForm(forms.Form):
    children_name = forms.CharField(max_length=255)
    children_birthday = forms.DateField()
    phone = forms.CharField(max_length=32)
    email = forms.EmailField()
    name = forms.CharField(max_length=255)
    comments = forms.CharField(max_length=255, required=False)
    agreement = forms.BooleanField()
