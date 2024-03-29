from django.conf.urls import include
from django.urls import re_path

urlpatterns = [
    re_path(r'^', include('uw_person_client.urls')),
]
