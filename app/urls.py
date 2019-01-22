from django.urls import path
from . import views

urlpatterns = [
    path('main_page', views.main_page, name='main_page'),
    path('', views.empty_page, name='empty_page'),
    path('login_page', views.login_page, name='login_page'),
    path('login_user', views.login_user, name='login_user'),
    path('do_logout', views.do_logout, name='do_logout'),
    path('java', views.java, name='java'),
    path('register', views.register, name='register'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('ajax_path', views.ajax_path, name='ajax_path'),
    path('notuniqlogin', views.notuniqlogin, name='notuniqlogin'),
]