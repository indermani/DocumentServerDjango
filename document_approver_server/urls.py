"""document_approver_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from knox.views import LogoutView

from .auth.views import LoginView

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include('document_receivings.urls')),
	url(r'^auth/login/$', LoginView.as_view()),
	url(r'^auth/logout/$', LogoutView.as_view()),
	url(r'^auth/logoutall/$', LogoutView.as_view())
]
