from django.urls import path
from deepagency import views

app_name='deepagency'

urlpatterns = [
    path('detail/', views.upload_image, name='detail'),
    path('start/', views.start, name='start'),
    path('', views.index, name='index'),
]