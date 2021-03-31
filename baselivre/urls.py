from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from core.views import Login, Logout, Home,  Register
from users.views import Index as UsersIndex, Create as UsersCreate 
from users.views import Update as UsersUpdate, UpdatePassword as UsersEditPassword
from users.views import Delete as UsersDelete

from groups.views import Index as GroupsIndex, Create as GroupsCreate 
from groups.views import Delete as GroupsDelete, Update as GroupsUpdate 


urlpatterns = [
    # core
    path('home/', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('password_change/',  auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',  auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',  auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',  auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^resetar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',  auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # admin
    path('admin/', admin.site.urls),
    # users
    path('users/', UsersIndex.as_view(), name='users_index'),
    path('users/new', UsersCreate.as_view(), name='users_new'),
    re_path('users/(?P<pk>\d+)/edit-password/', UsersEditPassword.as_view(), name='users_edit_password'),
    re_path('users/(?P<pk>\d+)/edit/', UsersUpdate.as_view(), name='users_update'),
    re_path('users/(?P<pk>\d+)/delete/', UsersDelete.as_view(), name='users_delete'),
    # groups
    path('groups/', GroupsIndex.as_view(), name='groups_index'),
    path('groups/new', GroupsCreate.as_view(), name='groups_new'),
    re_path('groups/(?P<pk>\d+)/edit/', GroupsUpdate.as_view(), name='groups_update'),
    re_path('groups/(?P<pk>\d+)/delete/', GroupsDelete.as_view(), name='groups_delete'),
]
