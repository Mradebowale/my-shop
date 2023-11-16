from django.contrib import admin
from .models import Booking, New, contactform
# Register your models here.

admin.site.register([Booking, contactform])

class NewsAdmin(admin.ModelAdmin):
    list_display = ["Headline"]
    list_filter = ["Headline"]
    search_fields = ["Headline"]
    prepopulated_fields = {"slug": ("Headline",)}

admin.site.register(New, NewsAdmin)

