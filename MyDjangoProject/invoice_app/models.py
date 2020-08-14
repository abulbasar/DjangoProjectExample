from django.db import models

# Create your models here

class CustomerModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tax_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices = [
        ("Active","Active"),
        ("Inactive", "Inactive"),
        ("Prospect", "Prospect")
    ], blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(blank=True, null=True)
