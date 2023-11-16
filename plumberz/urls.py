from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import homepage, booking, error, team, testimonial, service, contact, about

urlpatterns = [
    path("", homepage, name='home'),
    path("about/", about, name='about'),
    path("service/", service, name='services'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', error, name='404'),
    path('booking/', booking, name='booking'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact')
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)