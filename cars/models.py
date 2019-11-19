from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms

MODEL_CHOICES = [("SUV", "Sports Utility Vehicle"),
                    ("Sedan", "Sedan"),
                    ("Hatchback", "Hatchback"),
                    ("Mini SUV", "Mini Sports Utility Vehicle"),
                    ("Sports Car", "Sports Car")
                ]
MAKE_CHOICES = [
        ("Lamborghini", "Lamborghini"),
        ("Alfa Romeo", "Alfa Romeo"),
        ("Lexus", "Lexus"),
        ("Cadillac", "Cadillac"),
        ("Bentley", "Bentley"),
        ("Range Rover", "Range Rover"),
        ("Jaguar", "Jaguar"),
        ("Renault", "Renault"),
        ("Suzuki", "Maruti Suzuki"),
        ("Mahindra", "Mahindra"),
        ("Tata", "Tata"),
        ("Fiat", "Fiat"),
        ("Datsun", "Datsun"),
        ("Ford", "Ford"),
        ("Toyota", "Toyota"),
        ("Honda", "Honda"),
        ("Hyundai", "Hyundai"),
        ("Maserati", "Maserati"),
        ("Audi", "Audi"),
        ("Volkswagon", "Volkswagon"),
        ("BMW", "BMW"),
        ("Mini", "Mini")
    ]
FUEL_CHOICES = [
    ("Petrol", "Petrol"),
    ("Diesel", "Diesel"),
    ("Electric", "Electric"),
    ("Hybrid", "Hybrid")
]
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    model_type = models.CharField(choices = MODEL_CHOICES, max_length=200)
    make = models.CharField( choices = MAKE_CHOICES, max_length=200)
    ftype = models.CharField(choices = FUEL_CHOICES, max_length=10)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name
