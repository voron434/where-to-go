from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, Image


def balance_dims(height, width):
    if height > 200:
        coef = 200/height
        width = width * coef
        return 200, width
    return height, width


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ("file_image", )

    def file_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height}>'.
                           format(url=obj.file.url,
                                  width=obj.file.width,
                                  height=obj.file.height, )
                           )


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ("file_image", )

    def file_image(self, obj):
        img_dims = balance_dims(obj.file.height, obj.file.width)
        return format_html('<img src="{url}" width="{width}" height={height}>'.
                           format(url=obj.file.url,
                                  width=img_dims[1],
                                  height=img_dims[0], )
                           )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    readonly_fields = ("id", )


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
