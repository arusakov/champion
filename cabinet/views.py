from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from cabinet import forms, models


class GroupList(ListView):
    model = models.Group
    template_name = 'group_list.html'


class GroupCreate(CreateView):
    model = models.Group
    form_class = forms.GroupForm
    template_name = 'group_create.html'

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.pk})


class GroupDetail(DetailView):
    model = models.Group
    template_name = 'group_detail.html'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = models.Lesson.objects.filter(group=kwargs['object'])
        return context


class GroupLessonCreate(CreateView):
    model = models.Lesson
    form_class = forms.LessonForm
    template_name = 'lesson_create.html'
    pk_url_kwarg = 'group_id'

    def form_valid(self, form):
        form.instance.group = get_object_or_404(models.Group, pk=self.kwargs.get(self.pk_url_kwarg))
        return super(GroupLessonCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('group-detail', kwargs={'group_id': self.object.group_id})
