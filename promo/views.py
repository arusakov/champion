from django.views.generic.edit import FormView

from promo.forms import OrderForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):
        # TODO: send email
        print(form.cleaned_data)
        return super().form_valid(form)
