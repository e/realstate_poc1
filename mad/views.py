from django.http import HttpResponse
from django.shortcuts import render

from mad.forms import SearchForm
from mad.models import ApartmentRent

MADRID_COORDS = (40.416775, -3.703790)


def index(request):
    form = SearchForm(initial={'search_type': 'rent'})
    context = {'form': form}
    return render(request, "mad/index.html", context)


def rooms(request):
    map_center = request.GET.get('center', MADRID_COORDS)
    context = {'map_center': map_center}
    return render(request, "mad/rooms.html", context)


def rent(request):
    longitude = request.GET.get('longitude', MADRID_COORDS[0])
    latitude = request.GET.get('latitude', MADRID_COORDS[1])
    results = ApartmentRent.objects.all()
    context = {
        'latitude': latitude,
        'longitude': longitude,
        'results': results,
    }
    return render(request, "mad/rent.html", context)


def sale(request):
    return HttpResponse('hello')
