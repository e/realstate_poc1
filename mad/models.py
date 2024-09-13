from django.contrib.auth.models import User
from django.contrib.gis.db import models


class ApartmentSale(models.Model):
    address = models.CharField(max_length=1000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    price_sale = models.CharField(max_length=50)
    n_rooms = models.IntegerField()
    has_garage = models.BooleanField(default=False)
    has_garden = models.BooleanField(default=False)

    def __str__(self):
        return f"Apartment (sale) {self.id} - {self.address}"


class ApartmentRent(models.Model):
    address = models.CharField(max_length=1000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    price_rent = models.CharField(max_length=50)
    n_rooms = models.IntegerField()
    has_garage = models.BooleanField(default=False)
    has_garden = models.BooleanField(default=False)

    def __str__(self):
        return f"Apartment (rent) {self.id} - {self.address}"


class Room(models.Model):
    address = models.CharField(max_length=1000, blank=True)
    bed_size = models.CharField(max_length=20, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)

    def __str__(self):
        return f"Room {self.id} - {self.address}"


class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment_sale = models.ForeignKey(ApartmentSale, on_delete=models.SET_NULL, blank=True, null=True)
    apartment_rent = models.ForeignKey(ApartmentRent, on_delete=models.SET_NULL, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True)
    tags = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='img/avatars', blank=True)
    address = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"User profile {self.user.id} - {self.user.email}"
