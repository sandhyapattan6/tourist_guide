from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Booking, Contact, Brand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def login_user(request):
    return render(request, 'login.html')


def register_user(request):
    return render(request, 'register.html')


def logout_user(request):
    return render(request, 'index.html')


def packages(request):
    return render(request, 'packages.html')


def package_detail(request, name):

    data = {

        "goa":{
            "name":"Goa",
            "image":"images/goa.jpg",
            "description":"Enjoy beaches, nightlife and water sports.",
            "duration":"3 Days 2 Nights",
            "price":"₹12000"
        },

        "manali":{
            "name":"Manali",
            "image":"images/manali.jpg",
            "description":"Snow mountains and adventure sports.",
            "duration":"5 Days 4 Nights",
            "price":"₹18000"
        },

        "kerala":{
            "name":"Kerala",
            "image":"images/kerala.jpg",
            "description":"Backwaters and nature beauty.",
            "duration":"4 Days 3 Nights",
            "price":"₹15000"
        },

        "jaipur":{
            "name":"Jaipur",
            "image":"images/jaipur.jpg",
            "description":"Royal pink city palaces and forts.",
            "duration":"3 Days 2 Nights",
            "price":"₹10000"
        }

    }

    package = data.get(name)

    return render(request, "package_detail.html", package)

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

        # Send email to admin
        send_mail(
            "New Tour Booking",
            f"New booking from {name}\nEmail: {email}\nPhone: {phone}\nPackage: {package}\nDate: {date}",
            "sandhyapattan2006@gmail.com",
            ["sandhyapattan2006@gmail.com"],
            fail_silently=True,
        )

        return render(request, "success.html")

    # THIS LINE IS IMPORTANT
    return render(request, "book.html")

def services(request):

    services = [

        {
            "title": "Affordable Hotels",
            "icon": "🏨",
            "description": "Book comfortable and budget friendly hotels for your trip."
        },

        {
            "title": "Fast Travel",
            "icon": "✈️",
            "description": "Quick and safe travel arrangements to reach your destination."
        },

        {
            "title": "Food & Drinks",
            "icon": "🍽️",
            "description": "Enjoy delicious local food and refreshing drinks."
        },

        {
            "title": "Adventures",
            "icon": "🏔️",
            "description": "Experience trekking, rafting and thrilling adventure activities."
        },

        {
            "title": "24/7 Support",
            "icon": "📞",
            "description": "Our support team is available anytime to help you."
        }

    ]

    return render(request, "services.html", {"services": services})



def gallery(request):
    return render(request,"gallery.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save message to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email to admin
        send_mail(
            subject,
            message,
            email,
            ["sandhyapattan2006@gmail.com"],
            fail_silently=True,
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")

from .models import Brand

def home(request):
    brands = Brand.objects.all()  # fetch all brand logos
    return render(request, "index.html", {"brands": brands})


from django.shortcuts import render

def home(request):
    brands = [
        {"name": "Brand 1", "logo": "images/brand1.jpeg"},
        {"name": "Brand 2", "logo": "images/brand2.jpeg"},
        {"name": "Brand 3", "logo": "images/brand3.jpeg"},
        {"name": "Brand 4", "logo": "images/brand4.jpeg"},
        {"name": "Brand 5", "logo": "images/brand5.jpeg"},
    ]

    return render(request, 'index.html', {"brands": brands})

def package_detail(request, name):

    packages = {

        "Goa": {
            "duration": "3 Days / 2 Nights",
            "price": "₹15,000",
            "itinerary": [
                "Day 1: Arrival in Goa, hotel check-in, visit Baga Beach and Calangute Beach.",
                "Day 2: Visit Fort Aguada, Dudhsagar Waterfalls and enjoy water sports.",
                "Day 3: Visit local markets, shopping and departure."
            ]
        },

        "Manali": {
            "duration": "5 Days / 4 Nights",
            "price": "₹22,000",
            "itinerary": [
                "Day 1: Arrival and hotel check-in.",
                "Day 2: Visit Solang Valley and enjoy adventure sports.",
                "Day 3: Rohtang Pass sightseeing.",
                "Day 4: Hidimba Temple and local market.",
                "Day 5: Departure."
            ]
        },

        "Kerala": {
            "duration": "4 Days / 3 Nights",
            "price": "₹18,000",
            "itinerary": [
                "Day 1: Arrival and city tour.",
                "Day 2: Alleppey houseboat experience.",
                "Day 3: Munnar tea gardens and waterfalls.",
                "Day 4: Departure."
            ]
        },

        "Jaipur": {
            "duration": "4 Days / 3 Nights",
            "price": "₹20,000",
            "itinerary": [
                "Day 1: Arrival and hotel check-in.",
                "Day 2: Visit Amber Fort and Jal Mahal.",
                "Day 3: City Palace and Hawa Mahal sightseeing.",
                "Day 4: Local shopping and departure."
            ]
        }
    }

    package = packages.get(name)

    return render(request, "package_detail.html", {
        "package": package,
        "name": name
    })

def search_place(request):

    if request.method == "GET":

        query = request.GET.get("q")

        if query:
            query = query.lower()

            if query == "goa":
                return redirect("package_detail", name="Goa")

            elif query == "manali":
                return redirect("package_detail", name="Manali")

            elif query == "kerala":
                return redirect("package_detail", name="Kerala")

            elif query == "jaipur":
                return redirect("package_detail", name="Jaipur")

    return redirect("home")

def register_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect("login")

    return render(request, "register.html")

def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(request, "login.html", {"error":"Invalid username or password"})

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("home")

from django.shortcuts import render

def home(request):
    return render(request, "index.html")   # Home page

def reviews(request):
    return render(request, "reviews.html") # Reviews page

def about(request):
    return render(request, "about.html")

from django.shortcuts import render
from .models import Brand

def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})
    