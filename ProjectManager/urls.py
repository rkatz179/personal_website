from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'resume/', views.resume, name='resume'),
    url(r'currentprojects/', views.current_project, name='currentprojects'),
    url(r'hobbies/', views.interests, name='hobbies'),
]