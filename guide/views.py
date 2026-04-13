from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Booking, Contact, Brand


def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})


def packages(request):
    return render(request, "packages.html")


def package_detail(request, name):

    packages = {
        "Goa": {
            "duration": "3 Days / 2 Nights",
            "price": "₹15,000",
            "itinerary": [
                "Day 1: Arrival in Goa",
                "Day 2: Beaches and water sports",
                "Day 3: Departure"
            ]
        },
        "Manali": {
            "duration": "5 Days / 4 Nights",
            "price": "₹22,000",
            "itinerary": [
                "Day 1: Arrival",
                "Day 2: Solang Valley",
                "Day 3: Rohtang Pass",
                "Day 4: Local sightseeing",
                "Day 5: Departure"
            ]
        }
    }

    package = packages.get(name)

    return render(request, "package_detail.html", {
        "package": package,
        "name": name
    })


@login_required(login_url='login')
def book_package(request):
    if request.method == "POST":

        Booking.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            package=request.POST.get('package'),
            date=request.POST.get('date')
        )

        return render(request, "success.html")

    return render(request, "book.html")


def contact(request):
    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")


def register_user(request):

    if request.method == "POST":
        User.objects.create_user(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password")
        )
        return redirect("login")

    return render(request, "register.html")


def login_user(request):

    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect("home")

        return render(request, "login.html", {"error": "Invalid login"})

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def reviews(request):
    return render(request, "reviews.html")


def about(request):
    return render(request, "about.html")