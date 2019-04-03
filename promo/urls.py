from django.urls import include, path

from promo import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cabinet/', include('cabinet.urls')),
]
