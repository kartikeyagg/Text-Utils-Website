"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from . import views

# end points

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index, name = 'index'),
    # path('about/',views.about, name = 'index')
    path('analyze', views.removepunc, name = 'analyze'),

    path('capitilize_first', views.capfirst, name = 'capfirst'),
    path('new_line_remove', views.new_line_remove, name = 'new_line_remove'),
    path('space_remove', views.space_remove, name = 'space_remove'),
    path('char_count', views.char_count, name = 'char_count'),


]
























