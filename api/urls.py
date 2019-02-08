from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    # path('', views..as_view(), name=''),
    path('drf/', views.DRFViewSet.as_view(), name=''),
    # path('update/<int:pk>/', views..as_view(), name='')
    ]
