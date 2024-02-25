
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.logins,name='logins'),
    path('signup',views.signup,name='signup')
]
