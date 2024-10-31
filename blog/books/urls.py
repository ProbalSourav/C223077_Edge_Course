"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('books/list/', views.BookListView.as_view(), name='show book list'),
    path('initial_class/', views.MyView.as_view(), name='initial_class'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact_success/', lambda request: render(request,'success/contact_success.html'), name='contact_success'),
    # Login URL
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
]