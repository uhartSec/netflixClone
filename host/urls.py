from django.contrib import admin
from django.conf.urls import url, include
from . import views


"""
/admin
/host/login
"""


urlpatterns = [
	url(r'^login/', views.login_page, name='login-page'),
]
