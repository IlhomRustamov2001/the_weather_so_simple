from copy import deepcopy
from django.urls import path 
from .views import *
urlpatterns= [ 
    path('', index, name='index'),
    path('delete/<city_name>', delete, name='delete')
]