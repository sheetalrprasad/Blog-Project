from django.urls import path
from login_user_module import views
from django.contrib.auth import views as djangoView


app_name = 'login_user_module'

urlpatterns = [
    path('register/',views.register, name= 'register'),
    path('logout/',views.logout, name='logout_user')
]
