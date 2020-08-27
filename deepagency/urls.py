from django.urls import path
from deepagency import views

urlpatterns = [
    path('', views.index, name='index'),
]