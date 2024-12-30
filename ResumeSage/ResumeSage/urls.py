"""
URL configuration for ResumeSage project.

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
from django.contrib import admin
from django.urls import path, re_path
from ResumeSageApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/',views.sign_out, name='sign_out'),
    path('upload-file/', views.upload_page, name='upload-file'),
    path('generate-upload-url/', views.upload_file_to_s3, name='generate-upload-url'),
    path('review-resume/', views.llm_review, name='review-resume/'),
    re_path(r'^.*$', views.handle_unknown_routes),
]
