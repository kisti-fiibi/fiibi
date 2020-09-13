from django.urls import path
from deepagency import views

app_name='deepagency'

urlpatterns = [
    path('start/', views.start, name='start'),
    path('', views.index, name='index'),
]