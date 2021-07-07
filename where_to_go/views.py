from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from os import path

# from django.conf import settings
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


def place_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    imgs = [image.file.url for image in place.images.all()]
    jresponse_data = {"title": place.title, "imgs": imgs,
                      "description_short": place.description_short,
                      "description_long": place.description_long,
                      "coordinates": {"lng": place.coord_lng,
                                      "lat": place.coord_lat}
                      }
    json_dumps_params = {"ensure_ascii": False, "indent": 4}
    response = JsonResponse(jresponse_data, json_dumps_params=json_dumps_params)

    return HttpResponse(response, content_type="application/json")
