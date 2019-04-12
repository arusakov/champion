from django.urls import path

from cabinet import views

urlpatterns = [
    path('groups/list/', views.GroupList.as_view(), name='group-list'),
    path('groups/create/', views.GroupCreate.as_view(), name='group-create'),
    path('groups/<pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('groups/<pk>/lessons/create/', views.GroupLessonCreate.as_view(), name='lesson-create'),
]
