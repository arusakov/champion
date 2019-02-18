from django.views.generic.edit import CreateView

from promo.forms import RequestForm


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = RequestForm
    success_url = '/?success=1'
