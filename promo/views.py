from django.views.generic.edit import CreateView
from django.urls import reverse

from promo.forms import RequestForm


class IndexView(CreateView):
    template_name = 'promo.html'
    form_class = RequestForm

    def get_success_url(self, **kwargs):
        return reverse('promo-index') + '?success=1'
