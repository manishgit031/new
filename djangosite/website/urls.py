from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('learn', views.learn, name='learn'),
path('gallery', views.gallery, name='gallery'),
path('practice', views.practice, name='practice'),
path('login', views.login, name='login'),
]