from django.urls import path,include
from .views import index, get_query, get_query_home

urlpatterns = [
    path('', index, name="index"),
    path('query', get_query, name="get_query"),
    path('query_home', get_query_home, name="get_query_home")

]
