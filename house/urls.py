from django.urls import path

from house.views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('', AdvantagesListView.as_view(), name='home'),
]
