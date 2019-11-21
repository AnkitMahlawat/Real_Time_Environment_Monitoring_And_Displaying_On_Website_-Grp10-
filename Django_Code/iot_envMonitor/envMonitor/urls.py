from django.conf.urls import url
from views import Monitor

urlpatterns = [
    url('',Monitor,name='monitor')
]