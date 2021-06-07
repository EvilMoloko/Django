
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

def index(req):
    return render(req, 'myApp/index.html')


urlpatterns = [
    path('', include('main.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('blog/', include('blog.urls'), name='blog'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

