from django.urls import path

from . import views

app_name = "mad"
urlpatterns = [
    path("", views.index, name="index"),
    path("rooms", views.rooms, name="rooms"),
    path("rent", views.rent, name="rent"),
    path("sale", views.sale, name="sale"),
]
