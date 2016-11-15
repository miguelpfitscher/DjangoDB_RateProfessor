from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.rating, name='rating'),]


