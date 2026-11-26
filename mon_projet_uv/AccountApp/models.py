import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError(
            "La date de naissance doit être antérieure à la date du jour."
        )

class user(AbstractUser):
    pass

class doctor(user):
    phone=models.CharField(max_length=8)
    licence_number=models.CharField(max_length=6,unique=True)
    speciality=models.ManyToManyField('Speciality',related_name='doctors',null =True)

class patient(user):
    phone=models.CharField(max_length=8)
    birth_date=models.DateField(validators=[validate_past_date])
    national_id=models.CharField(max_length=8,unique=True)
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message="Le numéro de CIN doit contenir exactement 8 chiffres.",
            )
        ],
    )

class Speciality(models.Model):
    name = models.CharField(max_length=100)