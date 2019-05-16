from django.urls import path

from promo import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='promo-index'),
]
