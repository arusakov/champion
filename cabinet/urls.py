from django.urls import path

from cabinet import views

urlpatterns = [
    path('groups/list/', views.GroupList.as_view(), name='group-list'),
    path('groups/create/', views.GroupCreate.as_view(), name='group-create'),
    path('groups/<group_id>/', views.GroupDetail.as_view(), name='group-detail'),
    path('groups/<group_id>/lessons/create/', views.GroupLessonCreate.as_view(), name='lesson-create'),
    path('groups/<group_id>/lessons/<lesson_id>/', views.GroupLessonDelete.as_view(), name='lesson-delete'),
]
