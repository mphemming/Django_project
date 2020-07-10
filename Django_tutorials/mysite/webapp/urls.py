from . import views
from django.urls import path, re_path

urlpatterns = [
        re_path(r'^$',views.index, name='index')
        ]
