from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from cabinet.forms import GroupForm
from cabinet.models import Group, Schedule
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
    success_url = reverse_lazy('cabinet-group-list')

    def get_context_data(self, *args, **kwargs):
        context = super(GroupCreate, self).get_context_data(*args, **kwargs)
        context['week_days'] = Schedule.DAY_CHOICES
        return context

    def form_valid(self, form):
        Group.objects.create(course=form.cleaned_data['course'])
        return super(GroupCreate, self).form_valid(form)