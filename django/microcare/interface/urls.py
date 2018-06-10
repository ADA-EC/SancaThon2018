from django.urls import path
from . import views

app_name = 'interface'

urlpatterns = [
    path('', views.index, name='index'),
    path('locate', views.locate, name='locate'),
    path('look', views.look, name='look'),
    path('manage', views.manage, name='manage'),
    path('exit', views.exit, name='exit'),
]
