"""
URL configuration for one project.

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
from app import views as app_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',app_view.login,name='Login'),
    path('book',app_view.lib,name='book'),
    path('',app_view.book_login,name='booklogin'),
    path('bookdetails',app_view.bookdetails,name='Bookdetails'),
    path('updatebook/(?P<pk>\$',app_view.updatebook,name='updatebook'),
    path('deletebook/(?P<pk>\$',app_view.deletebook,name='deletebook'),
    path('takebook/(?P<pk>\$',app_view.takebook,name='takebook'),
    path('retainbook/(?P<pk>\$',app_view.retainbook,name='retainbook'),

    # app_view=fun_name,first-Login=browser-display,name=login-

]
