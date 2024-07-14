"""
URL configuration for ambientRead project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from proj import views

urlpatterns = [
    path("",views.home,name='home'),
    path("login/",auth_views.LoginView.as_view(template_name = 'login.html'),name="login"),
    path("admin/", admin.site.urls),
    path("signup/",views.signup,name="signup"),
     path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('upload/',views.upload_file,name='upload'),
    path('library/',views.library,name='library'),
    path('reader/<int:book_id>/', views.reader, name='reader'),
     path('analyze_sentiment/', views.analyze_sentiment, name='analyze_sentiment'),
]
