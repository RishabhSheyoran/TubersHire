from django.urls import path
from . import views

urlpatterns = [
    path('',views.youtubers1, name='youtubers1'),
    path('<int:id>',views.youtubers1_detail, name='youtubers1_detail'),
    path('search',views.search, name='search'),
]