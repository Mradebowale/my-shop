from django.contrib import admin
from .models import Booking, New, contactform
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "type"]
    list_filter = ["name", "email", "type"]
    search_fields = ["name"]

admin.site.register(Booking, ContactAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ["Headline"]
    list_filter = ["Headline"]
    search_fields = ["Headline"]
    prepopulated_fields = {"slug": ("Headline",)}

admin.site.register(New, NewsAdmin)


class ContactAdmin2(admin.ModelAdmin):
    list_display = ["names", "emails", "services"]
    list_filter = ["names", "emails", "services"]
    search_fields = ["names"]


admin.site.register(contactform, ContactAdmin2)