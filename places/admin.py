from django.contrib import admin

from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
