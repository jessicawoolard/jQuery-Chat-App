from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.HomeView.as_view(), name='chat/index'),
    # path('create/', views..as_view(), name=''),
    # path('update/<int:pk>/', views..as_view(), name='')
    ]
