"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blog.views import render_index_page, list_post, create_post, delete_post, edit_post, detail_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index_page),
    path('list/', list_post, name="list_post"),
    path('create/', create_post, name="create_post"),
    path('post/<int:pk>/', detail_post, name="detail_post"),
    path('post/<int:pk>/edit/', edit_post, name="edit_post"),
    path('post/<int:pk>/delete/', delete_post, name="delete_post"),    
]
