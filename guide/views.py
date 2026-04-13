from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Booking, Contact, Brand


# HOME
def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})


# LOGIN
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# REGISTER
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

    return render(request, "register.html")


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect("home")


# PACKAGES PAGE
def packages(request):
    return render(request, "packages.html")


# PACKAGE DETAIL
def package_detail(request, name):
    packages = {
        "Goa": {"price": "₹15000"},
        "Manali": {"price": "₹22000"},
        "Kerala": {"price": "₹18000"},
        "Jaipur": {"price": "₹20000"},
    }

    package = packages.get(name)
    return render(request, "package_detail.html", {"package": package, "name": name})


# 🔥 BOOKING (MAIN FIX)
@login_required(login_url='login')
def book_package(request):

    if request.method == "POST":
        try:
            Booking.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                package=request.POST.get('package'),
                date=request.POST.get('date')
            )

            # Email (safe)
            send_mail(
                "New Booking",
                "New booking received",
                "from@example.com",
                ["to@example.com"],
                fail_silently=True,
            )

            return render(request, "success.html")

        except Exception as e:
            return HttpResponse(f"ERROR: {e}")

    return render(request, "book.html")


# CONTACT
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


# OTHER PAGES
def services(request):
    return render(request, "services.html")

def gallery(request):
    return render(request, "gallery.html")

def reviews(request):
    return render(request, "reviews.html")

def about(request):
    return render(request, "about.html")


# SEARCH
def search_place(request):
    query = request.GET.get("q")

    if query:
        return redirect("package_detail", name=query.capitalize())

    return redirect("home")