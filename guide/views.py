from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .models import Booking, Contact, Brand


# ---------------- HOME ----------------
def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})


# ---------------- AUTH ----------------
def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


# ---------------- STATIC PAGES ----------------
def packages(request):
    return render(request, "packages.html")


def services(request):
    services_data = [
        {"title": "Affordable Hotels", "icon": "🏨", "description": "Budget friendly hotels."},
        {"title": "Fast Travel", "icon": "✈️", "description": "Quick and safe travel."},
        {"title": "Food & Drinks", "icon": "🍽️", "description": "Local food experience."},
        {"title": "Adventures", "icon": "🏔️", "description": "Trekking and rafting."},
        {"title": "24/7 Support", "icon": "📞", "description": "Anytime support."},
    ]
    return render(request, "services.html", {"services": services_data})


def gallery(request):
    return render(request, "gallery.html")


def about(request):
    return render(request, "about.html")


def reviews(request):
    return render(request, "reviews.html")


# ---------------- PACKAGE DETAIL ----------------
def package_detail(request, name):
    packages = {
        "goa": {
            "name": "Goa",
            "duration": "3 Days / 2 Nights",
            "price": "₹15,000",
            "itinerary": [
                "Day 1: Arrival, Baga Beach, Calangute Beach",
                "Day 2: Fort Aguada, Dudhsagar Falls, water sports",
                "Day 3: Shopping and departure"
            ]
        },
        "manali": {
            "name": "Manali",
            "duration": "5 Days / 4 Nights",
            "price": "₹22,000",
            "itinerary": [
                "Day 1: Arrival",
                "Day 2: Solang Valley",
                "Day 3: Rohtang Pass",
                "Day 4: Local sightseeing",
                "Day 5: Departure"
            ]
        },
        "kerala": {
            "name": "Kerala",
            "duration": "4 Days / 3 Nights",
            "price": "₹18,000",
            "itinerary": [
                "Day 1: Arrival",
                "Day 2: Alleppey houseboat",
                "Day 3: Munnar sightseeing",
                "Day 4: Departure"
            ]
        },
        "jaipur": {
            "name": "Jaipur",
            "duration": "4 Days / 3 Nights",
            "price": "₹20,000",
            "itinerary": [
                "Day 1: Arrival",
                "Day 2: Amber Fort, Jal Mahal",
                "Day 3: Hawa Mahal, City Palace",
                "Day 4: Shopping & departure"
            ]
        }
    }

    package = packages.get(name.lower())

    return render(request, "package_detail.html", {
        "package": package,
        "name": name
    })


# ---------------- BOOKING ----------------
@login_required(login_url='login')
def book_package(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        package = request.POST.get('package')
        date = request.POST.get('date')

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            package=package,
            date=date
        )


        return render(request, "success.html")

    return render(request, "book.html")


# ---------------- CONTACT ----------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        send_mail(
            subject,
            message,
            email,
            ["your_email@gmail.com"],
            fail_silently=True,
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")


# ---------------- SEARCH ----------------
def search_place(request):
    query = request.GET.get("q")

    if query:
        query = query.lower()

        if query in ["goa", "manali", "kerala", "jaipur"]:
            return redirect("package_detail", name=query)

    return redirect("home")