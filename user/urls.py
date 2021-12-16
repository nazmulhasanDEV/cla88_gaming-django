from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^ap/login/register/$', views.ap_login_register, name="apLoginRegister"),
    re_path(r'^ap/login/$', views.ap_login, name="apLogin"),
    re_path(r'^ap/logout/$', views.ap_logout, name="apLogout"),
    re_path(r'^ap/user/profile/$', views.ap_userProfile, name="apUserProfile"),
    re_path(r'^ap/change/user/name/$', views.ap_ChangeUserName, name="apChangeUserName"),

    re_path(r'^ap/change/user/pass/$', views.ap_ChangeUserPassword, name="apChangeUserPassword"),

    re_path(r'^ap/change/user/profile/pic/$', views.ap_ChangeUserProfilePic, name="apChangeUserProfilePic"),

]
