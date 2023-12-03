from django.shortcuts import render, redirect
from .forms import contactform1, bookingForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Booking, contactform

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



def contact2(request):
    if request.method == 'POST':
        form = contactform1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect(request, 'plumberz/404.html')
    else:
        form = contactform1()
    return render(request, 'plumberz/contact.html', {'form': form})




def booking(request):
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
        else:
            return redirect(request, 'plumberz/404.html')
    else:
        form = bookingForm()
    return render(request, 'plumberz/booking.html', {'form': form})
































































# def contact1(request):
#     if request.method == 'POST':
#         names = request.POST("names")
#         emails = request.POST("emails")
#         dates = request.POST("dates")
#         messages = request.POST("messages")
#         subjects = request.POST("subjects")

#         new_contact = contactform(names=names, emails=emails, subjects=subjects, dates=dates, messages=messages)
#         new_contact.save()
#         return render(request, "plumbers/contact.html")

        







        # form = contactform(request.POST, request.FILES)



    #     if form.is_valid():
    #         form.save()
    #         return redirect('booking')
    #     else:
    #         return HttpResponse("Something isn't right")
    # else:
    #     form = contactform()
    # return render(request, 'plumberz/booking.html', {'form': form})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        message = request.POST.get("message")
        type = request.POST.get("service")


        if len(name) > 100:
            messages.error(request, "name is too long")
            return redirect("contact")
        elif name == "":
            messages.error(request, "name cannot be left empty")
            return redirect("contact")
        elif type == "":
            messages.error(request, "Please select a service")
            return redirect("contact")
        elif date == "":
            messages.error(request, "type cannot be empty")
            return redirect("contact")
        elif message == "":
            messages.error(request, "message is too long")
            return redirect("contact")
        elif email =="":
            messages.error(request, "name is too long")
            return redirect("contact")
        else:
            Booking.objects.create(name=name, email=email, date=date, message=message, type=type)
            messages.success(request, "Thank you for contacting us")
            Booking.save()
            return redirect("home")
    else:
        return render(request, "plumberz/contact.html")

