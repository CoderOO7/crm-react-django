"""crmreactdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from rest_framework import routers                    # add this
from customers import views  
from django.conf.urls import url

""" router = routers.DefaultRouter()                      # add this
router.register(r'customers', views.CustomerView, 'customer')   
 """
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    url(r'^api/customers/$', views.customers_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
]
