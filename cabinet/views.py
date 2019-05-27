from django.views.generic import ListView, TemplateView

from promo.models import RequestInfo


class IndexView(TemplateView):
    template_name = 'cabinet.html'


class RequestList(ListView):
    model = RequestInfo
    template_name = 'request-list.html'
    paginate_by = 3

    def get_ordering(self):
        if self.request.GET.get('id') == 'desc':
            return '-id'
        if self.request.GET.get('id') == 'asc':
            return 'id'

        return '-id'
