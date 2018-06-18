from django.conf.urls import url
from . import views

urlpatterns = [url(r'^(?P<name>[a-z A-Z 1-9]+)/$',
                   views.detail, name='detail')]
