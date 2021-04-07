from django.contrib import admin
from main import models

admin.site.register([
    models.Student,
    models.Person,
    models.Society,
    models.Membership,
    models.Pizza,
    models.Topping,
    
    
])

# Register your models here.
