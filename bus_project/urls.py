
from django.contrib import admin
from django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns
from bus_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('bus_app/', views.PostsView.as_view()),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('Posts/',include(router.urls))

]

urlpatterns = format_suffix_patterns(urlpatterns)