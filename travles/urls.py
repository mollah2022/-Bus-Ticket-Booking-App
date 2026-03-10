from django.contrib import admin
from django.urls import path, include,re_path
from user.views import UserObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login/', UserObtainAuthToken.as_view(), name='login'),
    re_path('^api/', include('user.urls')),
    re_path('^api/', include('booking.urls')),
]
