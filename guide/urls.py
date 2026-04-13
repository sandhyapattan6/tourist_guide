from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    # ---------------- HOME ----------------
    path('', views.home, name="home"),

    # ---------------- AUTH ----------------
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),

    # ---------------- SEARCH ----------------
    path("search/", views.search_place, name="search"),

    # ---------------- PACKAGES ----------------
    path("packages/", views.packages, name="packages"),
    path("package/<str:name>/", views.package_detail, name="package_detail"),

    # ---------------- BOOKING ----------------
    path("book/", views.book_package, name="book_package"),

    # ---------------- SERVICES ----------------
    path("services/", views.services, name="services"),

    # ---------------- GALLERY ----------------
    path("gallery/", views.gallery, name="gallery"),

    # ---------------- CONTACT ----------------
    path("contact/", views.contact, name="contact"),

    # ---------------- REVIEWS ----------------
    path("reviews/", views.reviews, name="reviews"),

    # ---------------- ABOUT ----------------
    path("about/", views.about, name="about"),
]

# ---------------- MEDIA FILES ----------------
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)