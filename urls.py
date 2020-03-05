"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import man

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', man.home, name='home'),
    path('analyze',man.analyze,name='analyze'),
    #path('removepunc',man.removepunc, name='removepunc'),
    #path('fullcaps',man.capfirst,name='capfirst'),
    #path('newlineremove',man.newlineremove,name='newlineremove'),
    #path('extraspaceremover',man.spaceremover,name='spaceremover'),
   # path('charcount',man.charcount,name='charcount'),
]
