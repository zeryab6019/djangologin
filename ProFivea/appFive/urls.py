from django.urls import path
from appFive import views

app_name = 'appFivea'

urlpatterns = [
    path('register/',views.register, name = 'register_h'),
    path('user_login/', views.user_login, name = 'user_login_h')
]
