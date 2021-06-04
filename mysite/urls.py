
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path


def index(req):
    return render(req, 'myApp/index.html')


urlpatterns = [
    path('', include('main.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('blog/', include('blog.urls'), name='blog'),

    ]

