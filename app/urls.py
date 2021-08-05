from django.urls import path
from django.shortcuts import render, get_object_or_404
from .views import *

urlpatterns =[
    path('', index, name="index"),
    path('main', main, name="main"),
    path('admin-register', adminRegister, name="adminRegister"),
    path('admin-login', adminSignIn, name="admin_signin"),
    path('detail/<int:id>/', question_detail_view, name="main_detail"),
    path('question/<int:id>/', single_question, name="single_question"),
    path('login', signin, name="signin"),
    path('register', register, name="register"),
    path('logout', logout_view, name="logout"),
    path('change_password', change_password, name="change_password"),

    # post
    path('post', user_post, name="posts"),
]