from django.shortcuts import render, redirect
from .forms import bookingform
from django.http import HttpResponse
from django.contrib import messages
from .models import Booking

# Create your views here.

def homepage(request):
    return render(request, 'plumberz/index.html')

def testimonial(request):
    return render(request, 'plumberz/testimonial.html')


def about(request):
    return render(request, 'plumberz/about.html')

def service(request):
    return render(request, 'plumberz/service.html')


def team(request):
    return render(request, 'plumberz/team.html')

def contact(request):
    return render(request, 'plumberz/contact.html')


def booking(request):
    return render(request, 'plumberz/booking.html')


def error(request):
    return render(request, 'plumberz/404.html')


def contact(request):
    if request.method == 'POST':
        form = bookingform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booking')
        else:
            return HttpResponse("Something isn't right")
    else:
        form = bookingform()
    return render(request, 'plumberz/booking.html', {'form': form})


def booking2(request):
    if request.method == "POST":
        input_name = request.POST.get("name")
        input_email = request.POST.get("email")
        input_date = request.POST.get("date")
        input_message = request.POST.get("message")
        input_type = request.POST.get("service")


        if len(input_name) > 100:
            messages.error(request, "name is too long")
            return redirect("booking")
        elif input_name == "":
            messages.error(request, "name cannot be left empty")
            return redirect("booking")
        elif input_type == "":
            messages.error(request, "Please select a service")
            return redirect("booking")
        elif input_date == "":
            messages.error(request, "type cannot be empty")
            return redirect("booking")
        elif input_message == "":
            messages.error(request, "message is too long")
            return redirect("booking")
        elif input_email =="":
            messages.error(request, "name is too long")
            return redirect("booking")
        else:
            Booking.objects.create(name=input_name, email=input_email, date=input_date, message=input_message, type=input_type)
            messages.success(request, "Thank you for contacting us")
            return redirect("home")
    else:
        return render(request, "plumberz/booking.html")

