from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# from django.utils.text import slugify

from places.models import Place


def show_index(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def show_all_places(request):
    places = Place.objects.all()

    places_on_page = []
    for place in places:
        places_on_page.append({
            'coord_lng': place.coord_lng,
            'coord_lat': place.coord_lat,
            'title': place.title,
        })

    return render(request, "index.html", context={
        'places': places_on_page,
    })
