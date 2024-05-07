from django.urls import path
from App import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup')
]
