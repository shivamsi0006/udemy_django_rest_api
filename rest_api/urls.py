"""
URL configuration for rest_api project.

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
from django.urls import path,include
from updates.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updates/',update_model_detail_view,name='updates'),
    path('updates2/',JsonCBV.as_view(),name='genricview'),
    path('updates3/',SerializedDetailView.as_view(),name='detail_view'),
    path('updates4/',SerializedListView.as_view(),name='serialize'),
    path('api/updates/',include('updates.api.urls')),
    path('',home,name='home'),

]
