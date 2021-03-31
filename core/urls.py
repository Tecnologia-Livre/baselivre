from django.urls import include, re_path, path
from django.conf.urls import url

from . import views

urlpatterns = [
    re_path(r'login/$', views.Login.as_view()),
]