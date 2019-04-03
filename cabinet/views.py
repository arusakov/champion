from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from cabinet import forms, models

class GroupList(ListView):
    model = models.Group
    template_name = 'group_list.html'

class GroupCreate(CreateView):
    model = models.Group
    template_name = 'group_create.html'
    form_class = forms.GroupForm

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.pk})

class GroupDetail(DetailView):
    model = models.Group
    template_name = 'group_detail.html'

class GroupLessonCreate(CreateView):
    model = models.Lesson
    template_name = 'lesson_create.html'
    form_class = forms.LessonForm
