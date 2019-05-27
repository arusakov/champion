from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from cabinet import views

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='cabinet-index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='cabinet-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='cabinet-logout'),
    path('request/list/', login_required(views.RequestList.as_view()), name='cabinet-request-list'),
]
