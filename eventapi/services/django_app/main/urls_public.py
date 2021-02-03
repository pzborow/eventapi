from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from main.views import HomeView

urlpatterns = [path("", HomeView.as_view()), path("admin/", admin.site.urls)]
