from django.contrib import admin
from main.models import Tour, Claim, Image, Carousel, Article

admin.site.register(Tour)
admin.site.register(Claim)
admin.site.register(Article)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'carousel_image')

admin.site.register(Carousel, CarouselAdmin)

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('admin_image',)
    fields = ('title', 'admin_image', 'text', 'image', 'thumbnail')
    list_display = ('title', 'admin_image')

admin.site.register(Image, ImageAdmin)