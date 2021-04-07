from django.core import validators
from django.db import models

from django.core.validators import(
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug, 
)
from django.db.models.fields.related import ForeignKey

from main.validators import(
    validate_even_number
)
 

# Create your models here.
class Student(models.Model):
    GENDERS = (
        ('f', "Female"),
        ('m', "Male"),
        ('u', "uni")

    )
    name = models.CharField(max_length =  100)
    roll_no = models.IntegerField(unique = True)
    address = models.TextField(null = True)
    phone_no = models.CharField(blank = True, max_length = 15, null = True)
    email = models.CharField(max_length =  100, null = True, validators = [EmailValidator("Email address is not valid")])
    gender = models.CharField(max_length = 1, choices=GENDERS, null = True)
    age = models.IntegerField(
        null = True,
        validators= [
            MaxValueValidator(150),
            MinValueValidator(0),
            validate_even_number,
        ]
    )

    slug = models.CharField(max_length = 100, validators = [validate_slug], null=True)
    def __str__(self):
     return self.name


class  Topping(models.Model):
    name = models.CharField(max_length = 256) 
    def __str__(self):
      return self.name
class Pizza(models.Model):
     name = models.CharField(max_length = 256)
     price = models.IntegerField(validators=[
         MinValueValidator(0)     
     ])
     toppings = models.ManyToManyField('topping')

     def __str__(self):
      return self.name     

class Person(models.Model):
    name = models.CharField(max_length = 256) 
    def __str__(self):
      return self.name    

class Society(models.Model):
    name = models.CharField(max_length = 256) 
    def __str__(self):
      return self.name    


class Membership(models.Model):
    person_id = models.ForeignKey('Person', on_delete = models.CASCADE)   
    society_id = models.ForeignKey('Society', on_delete = models.CASCADE) 
    desgination = models.CharField(max_length = 256)     