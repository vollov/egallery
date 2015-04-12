from django.contrib import admin

from models import Image, Album

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
        
class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    #list_display = ["__unicode__", "title", "user", "created"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, ImageAdmin)
