from django.contrib import admin
from .models import Booking, New, contactform
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]
    list_filter = ["name", "email", "subject"]
    search_fields = ["name"]

admin.site.register(Booking, ContactAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ["Headline"]
    list_filter = ["Headline"]
    search_fields = ["Headline"]
    prepopulated_fields = {"slug": ("Headline",)}

admin.site.register(New, NewsAdmin)


class ContactAdmin2(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]
    list_filter = ["name", "email", "subject"]
    search_fields = ["name"]


admin.site.register(contactform, ContactAdmin2)