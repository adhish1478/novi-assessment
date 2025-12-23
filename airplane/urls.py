from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_airport, name="add_airport"),
    path("nth/", views.nth_node_view, name="nth-node"),
    path("longest/", views.longest_node_view, name="longest-node"),
    path("shortest/", views.shortest_between_view, name="shortest-node"),
]
