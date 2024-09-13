from django.contrib.gis import admin

from mad.models import ApartmentRent, Room, Advert

# admin.site.register(ApartmentSale)
admin.site.register(ApartmentRent, admin.GISModelAdmin)
admin.site.register(Room, admin.GISModelAdmin)
admin.site.register(Advert, admin.GISModelAdmin)
