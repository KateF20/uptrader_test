from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'slug', 'parent', 'url')
    list_filter = ('category', 'parent')
    prepopulated_fields = {'slug': ('name', )}
