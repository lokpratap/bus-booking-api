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
      path('register/', views.UserListView.as_view()),
      path('login/', views.UserLogin.as_view()),
      path('update/',views.UserUpdate.as_view()),
      path('delete/',views.DeleteSpecificUser.as_view()),
      path('allusers/',views.UserDetail.as_view()),
      path('currentusers/',views.Logged_in_users.as_view()),
      # path('currentusers/<int:pk>', views.Logged_in_users.as_view()),
      path('checkemailavailability/', views.CheckEmailAvail.as_view()),
      path('checkemailavailability/<int:pk>',views.CheckEmailAvail.as_view()),
      path('cityinfo/', views.CityInfo.as_view()),
      path('apiAvailableBuses', views.AvailableBuses.as_view()),
      path('getbusinfo', views.GetBusLayout.as_view()),
      path('getRtcUpdateFare/', views.getRTCUpdatedFare.as_view()),
      path('blockticket/', views.blockBusSeat.as_view()),
      path('getticket/', views.getTicketByETSTNumber.as_view()),
      path('cancelTicketConfirmation/', views.CancelTicketConfirmation.as_view()),
      path('cancelTicket/', views.CancelTicket.as_view()),

]
