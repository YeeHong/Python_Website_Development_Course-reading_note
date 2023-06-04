"""
URL configuration for firstproject project.

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
from django.urls import path
from myapp.views import sayhello # myapp.views => [root_path]/myapp/views.py
from myapp.views import hello2
from myapp.views import hello3
from myapp.views import hello4
from myapp.views import dice
from myapp.views import dice2
from myapp.views import dice3
from myapp.views import show
from myapp.views import filter

urlpatterns = [
    # path(url, function),
    # url name/<data_type1:parameter1>/<data_type2:parameter2>/......
    path('admin/', admin.site.urls), # default website ... (that website with rocket...)
    path('', sayhello),
    path('hello2/<str:username>', hello2), # http://127.0.0.1:8000/hello2/<str:username> Ex: http://127.0.0.1:8000/hello2/Tom
    path('hello3/<str:username>', hello3),
    path('hello4/<str:username>', hello4),
    path('dice/', dice),
    path('dice2/', dice2),
    path('dice3/', dice3),
    path('show/', show),
    path('filter/', filter),
]
