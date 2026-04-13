from django.db import models


# ---------------- BOOKING ----------------
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


# ---------------- CONTACT ----------------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


# ---------------- BRAND ----------------
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="brands/")
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# ---------------- REVIEW ----------------
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(default=5)  # 1 to 5 stars
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"