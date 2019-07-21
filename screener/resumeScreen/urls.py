from django.contrib import admin
from django.urls import path
from resumeScreen import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Main Routes
    path('', views.index, name="index"),
    path('signup/',views.user_registration,name='signup'),


    path('accounts/login/', auth_views.LoginView.as_view(),name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name="logout"),

    # path('upload/',views.upload,name="upload"),
    # path('resubmit/',views.resubmit,name="resubmit"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
