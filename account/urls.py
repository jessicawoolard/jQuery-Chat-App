from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('logout/', auth_views.logout, name=''),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    ]
