from django.contrib import admin
from photo import models

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = models.Photo
class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Photo)
    
