"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from firstapp import views

urlpatterns = [
path('', views.landing),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='Task1'),
    path('about/', views.about),
    path('login/', views.login, name='Task2'),
    path('welcome/', views.welcome),
    path('signup/', views.signup_view, name='Task3'),
    path('logintask3/', views.success),
    path('post', views.post),
    path('show/',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('logout/', views.logout),
]
