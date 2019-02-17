from django.views.generic.edit import FormView

from promo.forms import OrderForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = OrderForm

    def form_valid(self, form):
        # TODO: send email
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
