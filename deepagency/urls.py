from django.urls import path
from deepagency import views

app_name='deepagency'

urlpatterns = [
    path('', views.index, name='index'),
]