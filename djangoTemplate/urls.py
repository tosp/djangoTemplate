"""djangoTemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('base.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^tosp_auth/', include('tosp_auth.urls'))
]
