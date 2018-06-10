from django.urls import path
from . import views

app_name = 'interface'

urlpatterns = [
    path('', views.index, name='index'), 
    path('visualization', views.view, name='view'), 
    path('search', views.search, name='search'), 
    path('manage', views.manage, name='manage'), 
    path('exit', views.exit, name='exit'), 
]
