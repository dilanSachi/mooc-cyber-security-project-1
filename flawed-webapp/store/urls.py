from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin", views.admin, name="admin"),
    path("order", views.order, name="order")
]
