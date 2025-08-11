

# Register your models here.
from django.contrib import admin
from .models import Destination, Comment, DestinationImage

class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1   
    max_num = 10
    
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationImageInline]

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Comment)
admin.site.register(DestinationImage)
