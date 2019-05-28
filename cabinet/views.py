from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from cabinet.forms import GroupForm
from cabinet.models import Group
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


class GroupList(ListView):
    model = Group
    template_name = 'group-list.html'


class GroupCreate(FormView):
    template_name = 'group-create.html'
    form_class = GroupForm