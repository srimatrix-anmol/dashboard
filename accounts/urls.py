from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as account_views

urlpatterns = [
    path('', account_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
    ]