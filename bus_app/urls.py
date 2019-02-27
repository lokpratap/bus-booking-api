from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path , include

from rest_framework import routers






# from .views import PostsView
# router = routers.DefaultRouter()
# router.register('bus_app', PostsView,base_name='Posts' )
#
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index,name = 'index'),

]
