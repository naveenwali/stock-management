from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_item/',views.add_item),
    path('item_list/',views.item_list),
    path('supwisecount/',views.supwisecount),
    path('itemcount/',views.itemcount)
]
