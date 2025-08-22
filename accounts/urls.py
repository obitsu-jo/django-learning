from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('delete/', views.userdelete, name='user_delete'),
    path('confirm/', views.confirm_logout, name='confirm_logout'),
    path('', include('django.contrib.auth.urls'))
]