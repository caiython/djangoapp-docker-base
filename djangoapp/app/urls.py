from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('celery_hello_world/', views.celery_hello_world, name='celery_hello_world')
]
