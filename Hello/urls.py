

from django.urls import path, re_path
from Hello import views

urlpatterns = [

    re_path(r'^$', views.Hello, name='Hello'),
    re_path(r'^List/',views.list_view, name='list_view'),

    ]
