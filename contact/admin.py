from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','name', 'email',
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'id','name', 'email',
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'id', 'name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'name',
    search_fields = 'name',
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'name',
    