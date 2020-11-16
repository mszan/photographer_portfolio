from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from galleries.models import Gallery, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'visible', 'index', 'get_gallery', 'file_small_preview', 'file')
    search_fields = ('visible', 'index', 'file', 'gallery__title')
    readonly_fields = ('file_small',)

    def file_small_preview(self, obj):
        return format_html('<a href="/admin/galleries/image/{}/change"><img src="{}" width="150" height="150"/></a>', obj.id, obj.file_small.url)
    file_small_preview.short_description = 'Preview'
    file_small_preview.allow_tags = True

    def get_gallery(self, obj):
        return format_html('<a href="/admin/galleries/gallery/{}/change">{}</a>', obj.gallery.id, obj.gallery)
    get_gallery.short_description = 'Gallery'
    get_gallery.admin_order_field = 'gallery'


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'visible', 'main', 'index', 'title', 'get_images_count')

    def get_queryset(self, request):
        qs = super(GalleryAdmin, self).get_queryset(request)
        return qs.annotate(images_count=Count('images'))

    def get_images_count(self, obj):
        return format_html('<a href="/admin/galleries/image/?gallery_id={}">{}</a>', obj.id, obj.images_count)
    get_images_count.short_description = 'Images'


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)
