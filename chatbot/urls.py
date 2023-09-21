from django.urls import path,include
from .views import index, get_query

urlpatterns = [
    path('', index, name="index"),
    path('query', get_query, name="get_query")
]
